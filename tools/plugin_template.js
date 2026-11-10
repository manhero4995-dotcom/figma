const SPEC = __SPARK_SPEC__;

const FONT_STYLES = {
  400: "Regular", 500: "Medium", 600: "SemiBold",
  700: "Bold", 800: "ExtraBold", 900: "Black",
};
const fontCache = new Map();

function hexToRgb(hex) {
  let h = String(hex || "#000000").replace("#", "").trim();
  if (h.length === 3) h = h.split("").map((c) => c + c).join("");
  if (!/^[0-9a-fA-F]{6}$/.test(h)) h = "000000";
  return {
    r: parseInt(h.slice(0, 2), 16) / 255,
    g: parseInt(h.slice(2, 4), 16) / 255,
    b: parseInt(h.slice(4, 6), 16) / 255,
  };
}

function paint(hex, opacity) {
  return {
    type: "SOLID",
    color: hexToRgb(hex),
    opacity: opacity == null ? 1 : Math.max(0, Math.min(1, opacity)),
  };
}

async function loadFont(family, weight) {
  const key = family + "|" + weight;
  if (fontCache.has(key)) return fontCache.get(key);
  const style = FONT_STYLES[weight] || "Regular";
  const candidates = [[family, style], ["Inter", style], ["Inter", "Regular"]];
  for (const [fam, st] of candidates) {
    try {
      await figma.loadFontAsync({ family: fam, style: st });
      const font = { family: fam, style: st };
      fontCache.set(key, font);
      return font;
    } catch (err) {
      // try the next candidate
    }
  }
  throw new Error("No available font for " + family + " " + weight);
}

function applyPaints(node, el) {
  node.fills = el.fill && el.fill !== "none"
    ? [paint(el.fill, el.opacity)]
    : [];
  node.strokes = el.stroke ? [paint(el.stroke, el.opacity)] : [];
  if (el.stroke) {
    node.strokeWeight = el.sw || 1;
    try { node.strokeCap = el.cap === "butt" ? "NONE" : "ROUND"; } catch (e) {}
    try { node.strokeJoin = el.join === "miter" ? "MITER" : "ROUND"; } catch (e) {}
  }
}

function createNode(el, fonts) {
  if (el.type === "rect") {
    const node = figma.createRectangle();
    node.resize(Math.max(0.01, el.w), Math.max(0.01, el.h));
    const maxRadius = Math.min(el.w, el.h) / 2;
    if (el.rx) node.cornerRadius = Math.min(el.rx, maxRadius);
    applyPaints(node, el);
    return node;
  }
  if (el.type === "circle") {
    const node = figma.createEllipse();
    const d = Math.max(0.01, el.r * 2);
    node.resize(d, d);
    applyPaints(node, el);
    return node;
  }
  if (el.type === "path") {
    const node = figma.createVector();
    node.vectorPaths = [{ windingRule: "NONZERO", data: el.d }];
    applyPaints(node, el);
    return node;
  }
  if (el.type === "poly") {
    const xs = el.points.map((p) => p[0]);
    const ys = el.points.map((p) => p[1]);
    const minX = Math.min.apply(null, xs);
    const minY = Math.min.apply(null, ys);
    const data = "M " + el.points.map((p, i) =>
      (i ? "L " : "") + (p[0] - minX) + " " + (p[1] - minY)).join(" ") + " Z";
    const node = figma.createVector();
    node.vectorPaths = [{ windingRule: "NONZERO", data }];
    node.setPluginData("sparkOrigin", JSON.stringify({ x: minX, y: minY }));
    applyPaints(node, el);
    return node;
  }
  if (el.type === "text") {
    const node = figma.createText();
    node.fontName = fonts[el.font + "|" + el.weight];
    node.characters = el.text;
    node.fontSize = el.size;
    node.fills = [paint(el.color, el.opacity)];
    node.textAlignHorizontal = String(el.align || "left").toUpperCase();
    node.lineHeight = { unit: "PIXELS", value: el.lh || el.size * 1.35 };
    if (el.ls != null) node.letterSpacing = { unit: "PIXELS", value: el.ls };
    if (el.w && el.w > 0) {
      node.textAutoResize = "HEIGHT";
      node.resize(el.w, node.height);
    } else {
      node.textAutoResize = "WIDTH_AND_HEIGHT";
    }
    return node;
  }
  throw new Error("Unknown element type: " + el.type);
}

function positionNode(node, el) {
  if (el.type === "circle") {
    node.x = el.cx - el.r;
    node.y = el.cy - el.r;
  } else if (el.type === "poly") {
    const origin = JSON.parse(node.getPluginData("sparkOrigin") || '{"x":0,"y":0}');
    node.x = origin.x;
    node.y = origin.y;
  } else {
    node.x = el.x;
    node.y = el.y;
  }
}

function groupRuns(entries, frame) {
  let run = [];
  let runName = null;
  const flush = () => {
    if (!runName) { run = []; return; }
    if (run.length > 1) {
      const group = figma.group(run, frame);
      group.name = runName;
    } else if (run.length === 1) {
      run[0].name = runName + " / " + run[0].name;
    }
    run = [];
    runName = null;
  };
  for (const entry of entries) {
    if (entry.group && entry.group === runName) {
      run.push(entry.node);
    } else {
      flush();
      runName = entry.group || null;
      if (runName) run.push(entry.node);
    }
  }
  flush();
}

function addHeading(text, sub, x, y, fonts) {
  const title = figma.createText();
  title.fontName = fonts["Nunito|800"];
  title.characters = text;
  title.fontSize = 22;
  title.fills = [paint("#241A1F")];
  title.x = x;
  title.y = y;

  const caption = figma.createText();
  caption.fontName = fonts["Inter|500"];
  caption.characters = sub;
  caption.fontSize = 11;
  caption.fills = [paint("#6B7280")];
  caption.x = x;
  caption.y = y + 30;
}

function buildFrame(screen, role, x, y, fonts) {
  const frame = figma.createFrame();
  frame.name = role.title + " / " + screen.id + " · " + screen.title;
  frame.resize(screen.w, screen.h);
  frame.x = x;
  frame.y = y;
  frame.fills = [paint(screen.bg)];
  frame.clipsContent = true;

  const entries = [];
  for (const el of screen.elements) {
    const node = createNode(el, fonts);
    node.name = el.name || "Layer";
    frame.appendChild(node);
    positionNode(node, el);
    entries.push({ node, group: el.group || null });
  }
  groupRuns(entries, frame);
  return frame;
}

function uniquePageName(base) {
  let name = base;
  let n = 2;
  while (figma.root.children.some((p) => p.type === "PAGE" && p.name === name)) {
    name = base + " · " + n++;
  }
  return name;
}

async function main() {
  await figma.loadAllPagesAsync();

  const combos = new Set();
  for (const screen of SPEC.screens) {
    for (const el of screen.elements) {
      if (el.type === "text") combos.add(el.font + "|" + el.weight);
    }
  }
  ["Nunito|800", "Nunito|700", "Inter|400", "Inter|500"].forEach((c) => combos.add(c));

  const fonts = {};
  for (const combo of combos) {
    const parts = combo.split("|");
    fonts[combo] = await loadFont(parts[0], parseInt(parts[1], 10));
  }

  const createdPages = [];
  const firstFrames = [];
  const gap = 80;

  for (const role of SPEC.roles) {
    const screens = SPEC.screens.filter((s) => s.role === role.id);
    if (!screens.length) continue;

    const page = figma.createPage();
    page.name = uniquePageName(role.page);
    page.backgrounds = [paint("#EEF1F6")];
    figma.currentPage = page;

    let x = 0;
    const frames = [];
    for (const screen of screens) {
      addHeading(screen.id + " · " + screen.title,
        role.title + "  ·  " + screen.w + " × " + screen.h + "  ·  " + screen.description,
        x, 24, fonts);
      const frame = buildFrame(screen, role, x, 92, fonts);
      frames.push(frame);
      if (role.id === "system") firstFrames.push(frame);
      x += screen.w + gap;
    }
    createdPages.push({ page, frames });
  }

  if (createdPages.length) {
    figma.currentPage = createdPages[0].page;
    const focus = createdPages[0].frames;
    if (focus.length) figma.viewport.scrollAndZoomIntoView(focus);
  }

  figma.notify("SPARK UI/UX ready: " + SPEC.screens.length + " screens in " +
    createdPages.length + " pages", { timeout: 6000 });
  figma.closePlugin();
}

main().catch((err) => {
  console.error(err);
  figma.notify("SPARK UI/UX failed: " + err.message, { error: true, timeout: 12000 });
  figma.closePlugin();
});
