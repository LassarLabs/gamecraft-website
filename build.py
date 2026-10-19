#!/usr/bin/env python3
"""Builds the GameCraft website. Run `python3 build.py` to regenerate every page.

Page bodies are plain HTML strings; {{REPO}} and {{BLOB}} are replaced with
repository URLs when the page is written.
"""
from pathlib import Path

ROOT = Path(__file__).parent
REPO = "https://github.com/LassarLabs/gamecraft"
BLOB = REPO + "/blob/main"
VERSION = "0.3.0"

MARK = ('<svg viewBox="0 0 32 32" aria-hidden="true"><rect width="32" height="32" rx="6" fill="#16181d"/>'
        '<path d="M16 7 25 16 16 25 7 16Z" fill="#fff"/><path d="M16 12 20 16 16 20 12 16Z" fill="#2547c9"/></svg>')

NAV = [("features.html", "Features"), ("showcase.html", "Showcase"), ("unity.html", "Coming from Unity"),
       ("docs.html", "Docs"), ("roadmap.html", "Roadmap"), ("changelog.html", "News"), ("faq.html", "FAQ")]

TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>__TITLE__</title>
<meta name="description" content="__DESC__">
<meta property="og:title" content="__TITLE__">
<meta property="og:description" content="__DESC__">
<meta property="og:image" content="https://lassarlabs.github.io/gamecraft-website/assets/img/neon-city-aerial.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/site.css">
</head>
<body>
<header class="site-header">
  <div class="wrap header-in">
    <a class="wordmark" href="index.html">__MARK__ GameCraft</a>
    <nav class="nav" aria-label="Main">__NAV__</nav>
    <div class="header-actions">
      <a class="gh" href="{{REPO}}">GitHub</a>
      <a class="button primary" href="download.html">Download</a>
      <button class="menu-btn" aria-label="Menu" aria-expanded="false">Menu</button>
    </div>
  </div>
</header>
<main>
__BODY__
</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="footer-cols">
      <div>
        <a class="wordmark" href="index.html">__MARK__ GameCraft</a>
        <p>A free and open-source game engine, developed by LassarLabs.</p>
      </div>
      <div><h4>Engine</h4><a href="features.html">Features</a><a href="showcase.html">Showcase</a><a href="download.html">Download</a><a href="roadmap.html">Roadmap</a></div>
      <div><h4>Learn</h4><a href="docs.html">Documentation</a><a href="unity.html">Coming from Unity</a><a href="faq.html">FAQ</a><a href="changelog.html">News</a></div>
      <div><h4>Project</h4><a href="about.html">About</a><a href="{{REPO}}">Source code</a><a href="{{REPO}}/issues">Issue tracker</a><a href="{{BLOB}}/LICENSE">MIT License</a></div>
    </div>
    <div class="legal">
      <p>© 2026 LassarLabs. GameCraft is released under the MIT License.</p>
      <p>GameCraft is not affiliated with or endorsed by Unity Technologies. Unity is a trademark of Unity Technologies.</p>
    </div>
  </div>
</footer>
<script src="assets/js/site.js"></script>
</body>
</html>
"""


def page(file, title, desc, body):
    nav = "".join('<a href="%s">%s</a>' % n for n in NAV)
    html = (TEMPLATE.replace("__TITLE__", title).replace("__DESC__", desc).replace("__MARK__", MARK)
            .replace("__NAV__", nav).replace("__BODY__", body))
    html = html.replace("{{REPO}}", REPO).replace("{{BLOB}}", BLOB).replace("{{VERSION}}", VERSION)
    (ROOT / file).write_text(html)


def header(title, text):
    return '<section class="page-header"><div class="wrap"><h1>%s</h1><p>%s</p></div></section>' % (title, text)


def items(entries, cls="cols-3"):
    return ('<div class="%s">' % cls) + "".join(
        '<div class="item"><h3>%s</h3><p>%s</p></div>' % e for e in entries) + "</div>"


CSHARP = """<pre><code><span class="kw">using</span> UnityEngine;

<span class="kw">public class</span> <span class="ty">Spinner</span> : <span class="ty">MonoBehaviour</span>
{
    [<span class="ty">SerializeField</span>] <span class="kw">float</span> speed = <span class="nu">90f</span>;

    <span class="kw">void</span> Update()
    {
        transform.Rotate(<span class="nu">0f</span>, speed * <span class="ty">Time</span>.deltaTime, <span class="nu">0f</span>);
    }

    <span class="kw">void</span> OnTriggerEnter(<span class="ty">Collider</span> other)
    {
        <span class="ty">Debug</span>.Log(<span class="st">"Collected by "</span> + other.name);
        Destroy(gameObject);
    }
}</code></pre>"""

# ---------------------------------------------------------------- home
page("index.html", "GameCraft - free and open-source game engine",
     "GameCraft is a free and open-source 2D and 3D game engine with a full editor, C# scripting and export to desktop, web, Android and XR.", """
<section class="hero"><div class="wrap">
  <div class="hero-text">
    <h1>A free and open-source game engine</h1>
    <p>Make 2D and 3D games in a full-featured editor, write gameplay in C#, and export to desktop, web, Android and XR. GameCraft runs entirely on your own computer. There is no account to create and nothing to pay.</p>
    <div class="buttons">
      <a class="button primary" href="download.html">Download GameCraft</a>
      <a class="button secondary" href="features.html">Explore features</a>
    </div>
    <p class="small">macOS on Apple Silicon. Windows and Linux can be built from source.</p>
  </div>
  <figure class="hero-image">
    <img src="assets/img/neon-city-aerial.jpg" alt="A night city with lit skyscrapers, elevated roads and a central plaza, rendered in GameCraft" width="1920" height="1080">
    <figcaption>Neon City, a demo scene built in the GameCraft editor and rendered in real time.</figcaption>
  </figure>
</div></section>

<section class="section"><div class="wrap">
  <div class="section-intro">
    <h2>Everything in one editor</h2>
    <p>GameCraft combines a native engine written in Rust, the .NET runtime for scripting, and a desktop editor. The parts are developed together and tested together.</p>
  </div>
  """ + items([
      ("Rendering", "Physically based rendering on Metal, Vulkan, DirectX 12 and WebGPU, with post-processing, reflection probes, baked lighting and a node-based shader editor."),
      ("C# scripting", "Scripts compile when you save and run on .NET 10. Hot reload keeps the values in your fields, and you can attach a debugger."),
      ("Physics", "3D and 2D rigid bodies, joints, a character controller, raycasts and a collision matrix with 32 layers."),
      ("Animation", "Animator state machines, skeletal animation from glTF and FBX, blend shapes, inverse kinematics and a Timeline editor."),
      ("Effects", "Particle systems with collisions, a GPU particle graph with up to a million particles, and trail renderers."),
      ("Multiplayer", "Networked objects, synchronised variables and remote procedure calls over UDP, with host, server and client modes."),
  ]) + """
  <p style="margin-top:40px"><a href="features.html">See the full feature list</a></p>
</div></section>

<section class="section alt"><div class="wrap">
  <div class="row">
    <figure class="figure">
      <img src="assets/img/editor.jpg" alt="The GameCraft editor with the Hierarchy, Scene view and engine view open" width="1776" height="853" loading="lazy">
      <figcaption>The editor in Play mode. The panel on the right is rendered by the engine itself.</figcaption>
    </figure>
    <div>
      <h2>A familiar editor</h2>
      <p>Hierarchy, Inspector, Scene and Game views, a Project browser and a Console, arranged in panels you can dock anywhere. If you have used a modern game editor before, you already know where things are.</p>
      <p>Add components, edit values while the game runs, build prefabs, and press Play to run the scene in the real engine rather than a preview.</p>
    </div>
  </div>
  <div class="row flip">
    <div>""" + CSHARP + """</div>
    <div>
      <h2>Bring your Unity projects</h2>
      <p>GameCraft can import Unity scenes, prefabs, materials, animations and <code>.unitypackage</code> files, and it runs scripts written against the common parts of the <code>UnityEngine</code> API without changes.</p>
      <p>An import report lists everything that was converted and everything that was skipped.</p>
      <p><a href="unity.html">Read the migration guide</a></p>
    </div>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="cols-2">
    <div>
      <h2>Export to every platform you can test</h2>
      <p>One project builds for several targets from the editor or the command line. Exported games are self-contained and do not need GameCraft to be installed.</p>
      <p><a href="features.html#platforms">Platform details</a></p>
    </div>
    <table class="facts">
      <tr><th>Desktop</th><td>macOS, Windows, Linux</td></tr>
      <tr><th>Web</th><td>WebAssembly with WebGPU</td></tr>
      <tr><th>Mobile</th><td>Android (arm64)</td></tr>
      <tr><th>XR</th><td>OpenXR headsets</td></tr>
      <tr><th>License</th><td>MIT, with no royalties or fees</td></tr>
    </table>
  </div>
</div></section>

<section class="section alt"><div class="wrap">
  <div class="section-intro"><h2>News</h2></div>
  <ul class="news">
    <li><time>October 2026</time><div><h3>Live build sessions</h3><p>The editor can now be driven by a command file, so whole scenes can be built from a script while you watch. The Neon City demo was made this way.</p></div></li>
    <li><time>October 2026</time><div><h3>GameCraft 0.3</h3><p>Unity project import, the UnityEngine and UnityEditor compatibility layers, post-processing, Shader Graph, Timeline, and new Windows, Linux, Web, Android and XR targets.</p></div></li>
  </ul>
  <p style="margin-top:24px"><a href="changelog.html">All news</a></p>
</div></section>

<section class="section"><div class="wrap">
  <div class="cols-3">
    <div class="item"><h3>Get the source</h3><p>GameCraft is developed in the open on GitHub. <a href="{{REPO}}">Browse the repository</a>.</p></div>
    <div class="item"><h3>Report a problem</h3><p>Found a bug or missing feature? <a href="{{REPO}}/issues">Open an issue</a>.</p></div>
    <div class="item"><h3>Contribute</h3><p>Changes are welcome. Every change needs a test. <a href="about.html">How to contribute</a>.</p></div>
  </div>
</div></section>
""")

# ---------------------------------------------------------------- features
page("features.html", "Features - GameCraft", "A complete list of GameCraft features.",
     header("Features", "An overview of what GameCraft can do today. Known gaps are listed in the <a href=\"{{BLOB}}/docs/LIMITATIONS.md\">limitations document</a>.") + """
<section class="section"><div class="wrap">
  <h2>Rendering</h2>
  <p class="section-intro">A forward renderer built on wgpu, running on Metal, Vulkan, DirectX 12 and WebGPU.</p>
  """ + items([
      ("Post-processing", "Bloom, tone mapping (including ACES), colour adjustments, white balance, lift/gamma/gain, vignette, chromatic aberration, film grain, ambient occlusion, depth of field and motion blur, controlled by volumes."),
      ("Lighting", "Directional, point and spot lights with shadows. Realtime and baked reflection probes, light probes, and lightmaps from a path tracer."),
      ("Shader Graph", "A node editor with around 50 nodes. Graphs compile to WGSL, and each material can override graph properties."),
      ("Cameras", "Multiple cameras with depth order, viewport rectangles, culling masks, overlay cameras and render textures."),
      ("Performance", "LOD groups, occlusion culling, compressed textures and GPU skinning."),
      ("Particles", "CPU particle systems with world and plane collisions, a GPU particle graph, and trail renderers."),
  ]) + """
</div></section>
<section class="section alt"><div class="wrap">
  <h2>Scripting</h2>
  <p class="section-intro">Gameplay is written in C#. The .NET 10 runtime is hosted inside the engine and the Roslyn compiler runs when you save.</p>
  """ + items([
      ("Two APIs", "Use the GameCraft SDK, or write against the UnityEngine-compatible API with MonoBehaviour, coroutines and serialized fields."),
      ("Hot reload", "Change a script while the game is running. Serialized field values are kept."),
      ("Debugging", "Attach a .NET debugger to Play mode with full symbol information."),
      ("Jobs and ECS", "A job system with native containers and safety checks, Burst-compatible attributes, Unity.Mathematics and a minimal entity component system."),
      ("Editor scripts", "Scripts in Editor folders can add custom inspectors, editor windows, menu items and property drawers."),
      ("Packages", "Share code as packages from a local folder or a package registry, with dependency resolution and integrity checks."),
  ]) + """
</div></section>
<section class="section"><div class="wrap">
  <h2>Tools</h2>
  <p class="section-intro">Built into the editor, with no extra installation.</p>
  """ + items([
      ("Timeline", "Sequence animation, activation, audio, signals and camera shots."),
      ("Virtual cameras", "Priorities, follow and look-at targets, damping, dolly tracks, noise and blending."),
      ("Mesh editing", "Edit vertices, edges and faces; extrude, inset and subdivide; edit UVs."),
      ("Animation rigging", "Two-bone IK, aim and parent constraints on top of animated characters."),
      ("Terrain", "Sculpt and paint terrain, place vegetation and stream regions."),
      ("Navigation", "Bake navigation meshes and move agents around obstacles."),
      ("Audio", "Spatial audio and a mixer with groups, effects, sends and snapshots."),
      ("User interface", "Canvas-based UI with text, buttons, inputs, toggles, sliders, dropdowns and scroll views."),
      ("Localization", "String and asset tables, plural rules per language, and CSV import and export."),
  ]) + """
</div></section>
<section class="section alt" id="platforms"><div class="wrap">
  <h2>Platforms</h2>
  <p class="section-intro">How each export target is tested.</p>
  <div class="table-wrap"><table class="data">
    <tr><th>Platform</th><th>Status</th><th>Testing</th></tr>
    <tr><td>macOS (Apple Silicon)</td><td class="yes">Supported</td><td>Editor and exported games, including an automated test that creates a game from scratch in the installed app.</td></tr>
    <tr><td>Windows x64</td><td class="yes">Supported</td><td>Cross-compiled player, checked under Wine.</td></tr>
    <tr><td>Linux arm64 and x64</td><td class="yes">Supported</td><td>Full test suite in Docker; exported games in clean containers.</td></tr>
    <tr><td>Web</td><td class="yes">Supported</td><td>WebAssembly and WebGPU, with C# on the .NET WebAssembly runtime.</td></tr>
    <tr><td>Android arm64</td><td class="yes">Supported</td><td>Signed APK on the Android emulator with scripted input.</td></tr>
    <tr><td>OpenXR</td><td class="yes">Supported</td><td>Stereo rendering against the Monado runtime.</td></tr>
    <tr><td>iOS</td><td class="planned">Not yet</td><td>Requires Xcode with the iOS SDK and an Apple Developer account.</td></tr>
    <tr><td>Consoles</td><td class="planned">Not yet</td><td>Console SDKs are only available to licensed developers.</td></tr>
  </table></div>
</div></section>
""")

# ---------------------------------------------------------------- showcase
page("showcase.html", "Showcase - GameCraft", "Scenes made with GameCraft.",
     header("Showcase", "Scenes made with GameCraft. If you have made something, open an issue and we may feature it here.") + """
<section class="section"><div class="wrap">
  <h2>Neon City</h2>
  <p class="section-intro">A night city with 189 towers, elevated roads, 44 flying cars and 90 pedestrians, built from primitive shapes, four Shader Graph materials and three C# scripts. The scene was assembled in the editor by a script using live build sessions, one undoable step per object.</p>
  <div class="gallery">
    <figure class="figure wide"><img src="assets/img/neon-city-aerial.jpg" alt="Aerial view of Neon City" loading="lazy"><figcaption>Aerial view of the skyline and plaza.</figcaption></figure>
    <figure class="figure"><img src="assets/img/neon-city-1200.jpg" alt="Neon City at street level" loading="lazy"><figcaption>Street level, with procedural building windows and holographic billboards.</figcaption></figure>
    <figure class="figure"><img src="assets/img/neon-city-120.jpg" alt="The plaza in Neon City" loading="lazy"><figcaption>The plaza. The wet ground reflects the city through a reflection probe.</figcaption></figure>
  </div>
</div></section>
<section class="section alt"><div class="wrap">
  <h2>How it was made</h2>
  <div class="cols-2" style="margin-top:32px">
    <div class="prose">
      <h3>Materials</h3>
      <p>The building windows come from a single Shader Graph that divides each wall into floors and bays using its world position, then lights a random selection of them. The billboards use an animated graph with moving noise and scan lines. The plaza floor varies its smoothness to form puddles.</p>
      <h3>Scripts</h3>
      <p>Three C# scripts written against the UnityEngine API move the cars along their lanes, let pedestrians wander the plaza, and drift the camera slowly through the scene.</p>
    </div>
    <div>
      <h3>Build it yourself</h3>
      <p>The generator script is in the repository. Point the editor at its output folder and the scene builds in front of you.</p>
<pre><code>python3 tools/demo/neon_city.py ~/NeonCity
GAMECRAFT_LIVE_DIR=~/NeonCity gamecraft</code></pre>
      <p style="margin-top:16px"><a href="{{BLOB}}/tools/demo/neon_city.py">View neon_city.py</a></p>
    </div>
  </div>
</div></section>
""")

# ---------------------------------------------------------------- unity
page("unity.html", "Coming from Unity - GameCraft", "How to move a Unity project to GameCraft and what is supported.",
     header("Coming from Unity", "GameCraft reads Unity's file formats and implements a large part of its scripting API. This page explains what carries over and how to migrate a project.") + """
<section class="section"><div class="wrap prose">
  <h2>Importing a project</h2>
  <ol>
    <li>In Unity, export your assets as a <code>.unitypackage</code>, or keep the project folder.</li>
    <li>In GameCraft, choose <b>Assets &gt; Import Unity Project</b> or <b>Import Unity Package</b>. You can also use <code>gamecraft-cli unity-import</code>.</li>
    <li>Check the import report in the Console. It lists what was converted, what was skipped and why.</li>
    <li>Press Play. Scripts compile against the compatibility layer and run in the engine.</li>
  </ol>

  <h2>What is imported</h2>
  <ul>
    <li>Scenes and prefabs, including nested prefabs, overrides and removed components</li>
    <li>Materials (Standard and URP), animation clips and animator controllers</li>
    <li>ScriptableObject assets, render textures, UI canvases and particle systems</li>
    <li>Audio mixers and Localization package tables</li>
    <li>Asset references, resolved through the GUIDs in <code>.meta</code> files</li>
  </ul>

  <h2>Scripting API</h2>
  <p>Scripts using the supported parts of <code>UnityEngine</code> compile without changes. This includes MonoBehaviour messages, <code>GetComponent</code>, transforms, coroutines, serialized fields, ScriptableObject, UnityEvent, physics, input and touch, cameras, materials, UI, scene management, Netcode for GameObjects, Addressables and Localization. A script that uses something unsupported fails to compile with an error naming the missing member.</p>
  """ + CSHARP + """

  <h2>Editor extensions</h2>
  <p>Scripts in <code>Editor</code> folders run inside the GameCraft editor. Custom inspectors, <code>EditorGUILayout</code>, editor windows, menu items and property drawers are supported. UI Toolkit editors, <code>Handles</code> and scene-view drawing are not.</p>

  <h2>Not supported</h2>
  <ul>
    <li>Precompiled <code>.dll</code> plugins and native libraries. Packages must ship C# source.</li>
    <li>The Unity Asset Store and Unity online services. Assets exported as a <code>.unitypackage</code> can be imported.</li>
    <li>iOS and console platforms.</li>
  </ul>
  <p>The complete checklist, with the test that covers each item, is in <a href="{{BLOB}}/docs/UNITY_PARITY.md">UNITY_PARITY.md</a>: 66 of 73 items are done, and the remaining 7 depend on outside accounts, hardware or proprietary services.</p>
</div></section>
""")

# ---------------------------------------------------------------- docs
page("docs.html", "Documentation - GameCraft", "Install GameCraft, build it from source and make your first game.",
     header("Documentation", "Getting started with GameCraft. The full manuals live in the repository.") + """
<section class="section"><div class="wrap">
  <div class="cols-2">
    <div class="prose">
      <h2>Your first project</h2>
      <ol>
        <li>Open GameCraft and choose <b>New Project</b>. Pick the 3D Core template.</li>
        <li>Choose <b>GameObject &gt; 3D Object &gt; Cube</b> and add a Rigidbody in the Inspector.</li>
        <li>Choose <b>Assets &gt; Create &gt; MonoBehaviour Script</b> and open it in the script editor.</li>
        <li>Press <b>Play</b> to run the scene.</li>
        <li>Choose <b>File &gt; Build Settings</b> and click <b>Build</b> to export a standalone game.</li>
      </ol>
    </div>
    <div class="prose">
      <h2>Building from source</h2>
      <p>You need Node 22.19 or later, the stable Rust toolchain and the .NET 10 SDK. On macOS you also need the Xcode command-line tools.</p>
<pre><code>git clone {{REPO}}.git
cd gamecraft
npm install
source tools/env.sh
npm run dotnet:build
npm run tauri:dev</code></pre>
    </div>
  </div>
</div></section>
<section class="section alt"><div class="wrap">
  <div class="cols-2">
    <div class="prose">
      <h2>Command line</h2>
<pre><code>gamecraft-cli build &lt;project&gt; --target web
gamecraft-cli unity-import &lt;unity-project&gt; &lt;output&gt;
gamecraft-cli bake-lighting &lt;project&gt;
gamecraft-cli package search &lt;query&gt;</code></pre>
    </div>
    <div class="prose">
      <h2>Running the tests</h2>
<pre><code>tools/quality-gates.sh     # everything
cargo test --workspace      # engine
npx vitest run              # editor
tools/linux-test.sh         # Linux, in Docker</code></pre>
    </div>
  </div>
</div></section>
<section class="section"><div class="wrap">
  <h2>Manuals</h2>
  <div class="table-wrap" style="margin-top:24px"><table class="data">
    <tr><th>Document</th><th>Contents</th></tr>
    <tr><td><a href="{{BLOB}}/docs/USER_GUIDE.md">User guide</a></td><td>The editor, its panels and workflows</td></tr>
    <tr><td><a href="{{BLOB}}/docs/SCRIPTING.md">Scripting reference</a></td><td>The GameCraft SDK and the UnityEngine-compatible API</td></tr>
    <tr><td><a href="{{BLOB}}/docs/ARCHITECTURE.md">Architecture</a></td><td>How the engine, editor and runtime fit together</td></tr>
    <tr><td><a href="{{BLOB}}/docs/UNITY_PARITY.md">Unity parity</a></td><td>Unity features and their status</td></tr>
    <tr><td><a href="{{BLOB}}/docs/LIMITATIONS.md">Limitations</a></td><td>Features that are partial or missing</td></tr>
    <tr><td><a href="{{BLOB}}/CHANGELOG.md">Changelog</a></td><td>Changes in each release</td></tr>
  </table></div>
</div></section>
""")

# ---------------------------------------------------------------- download
page("download.html", "Download - GameCraft", "Download GameCraft.",
     header("Download", "GameCraft {{VERSION}}. The application includes everything it needs: the .NET runtime, the script compiler, the game player and the command-line tools.") + """
<section class="section"><div class="wrap">
  <div class="table-wrap"><table class="data">
    <tr><th>Platform</th><th>Download</th><th>Notes</th></tr>
    <tr><td>macOS, Apple Silicon</td><td><a href="{{REPO}}/releases">Releases page</a></td><td>macOS 12 or later. Pre-built packages are published on the Releases page; until the first one is available, build from source. The app is not notarized yet, so the first time you open it, right-click it and choose Open.</td></tr>
    <tr><td>Windows</td><td><a href="docs.html">Build from source</a></td><td>Games can already be exported for Windows from macOS.</td></tr>
    <tr><td>Linux</td><td><a href="docs.html">Build from source</a></td><td>Games can already be exported for Linux from macOS.</td></tr>
    <tr><td>Source code</td><td><a href="{{REPO}}">github.com/LassarLabs/gamecraft</a></td><td>MIT License.</td></tr>
  </table></div>
</div></section>
<section class="section alt"><div class="wrap prose">
  <h2>System requirements</h2>
  <table class="facts">
    <tr><th>Operating system</th><td>macOS 12 or later on Apple Silicon</td></tr>
    <tr><th>Graphics</th><td>Metal, Vulkan, DirectX 12 or WebGPU</td></tr>
    <tr><th>Disk space</th><td>About 200 MB for the application</td></tr>
    <tr><th>Internet</th><td>Not required</td></tr>
  </table>
  <h2>Security</h2>
  <p>C# scripts and packages run with the same permissions as the editor and are not sandboxed. Only open projects and install packages from sources you trust.</p>
</div></section>
""")

# ---------------------------------------------------------------- roadmap
def milestone(state, cls, title, entries):
    return ('<li><div><span class="state %s">%s</span></div><div><h3>%s</h3><ul>%s</ul></div></li>'
            % (cls, state, title, "".join("<li>%s</li>" % e for e in entries)))


page("roadmap.html", "Roadmap - GameCraft", "What is planned for GameCraft.",
     header("Roadmap", "What is finished, what we are working on next, and what is waiting on outside partners. Suggestions are welcome in the <a href=\"{{REPO}}/issues\">issue tracker</a>.") + """
<section class="section"><div class="wrap"><ul class="milestones">
""" + milestone("In progress", "", "Polish", ["Rich text, scroll bars and world-space UI canvases", "More particle modules, including sub-emitters", "Blending between Timeline clips", "2D lights and gamepad vibration"])
     + milestone("In progress", "", "Automation", ["Live build sessions that keep running when the editor window is hidden", "Scripted scene pipelines"])
     + milestone("Planned", "planned", "Releases", ["Signed and notarized macOS builds", "Signed Windows builds", "Automatic updates"])
     + milestone("Planned", "planned", "Community", ["A public package registry", "Sample game templates"])
     + milestone("Waiting on partners", "no", "iOS", ["Requires Xcode with the iOS SDK and an Apple Developer account"])
     + milestone("Waiting on partners", "no", "Consoles", ["Requires acceptance into the PlayStation, Xbox and Nintendo developer programmes", "Xbox is the most likely first target, since it uses DirectX 12"])
     + milestone("Done", "yes", "0.3", ["Unity project import and compatibility layers", "Post-processing, global illumination and Shader Graph", "Timeline, virtual cameras, GPU particles, mesh editing and rigging", "Windows, Linux, Web, Android and OpenXR export", "Package registry, Addressables, audio mixer, multiplayer and localization"]) + """
</ul></div></section>
""")

# ---------------------------------------------------------------- news
page("changelog.html", "News - GameCraft", "News and release notes for GameCraft.",
     header("News", "Release notes and project updates. Detailed changes are in the <a href=\"{{BLOB}}/CHANGELOG.md\">changelog</a>.") + """
<section class="section"><div class="wrap"><ul class="news">
  <li><time>October 2026</time><div><h3>Live build sessions</h3><p>Start the editor with <code>GAMECRAFT_LIVE_DIR</code> set and it runs the commands written to a file in that folder: creating projects, objects, materials and scripts, saving and playing. Each command goes through the normal editor actions and can be undone. The Neon City demo shows what it can do.</p></div></li>
  <li><time>October 2026</time><div><h3>GameCraft 0.3</h3><p>The largest release so far. It adds Unity project import and the UnityEngine and UnityEditor compatibility layers, post-processing, reflection and light probes, baked lighting, Shader Graph, LOD and occlusion culling, Timeline, virtual cameras, GPU particles, mesh editing, animation rigging, and export to Windows, Linux, Web, Android and OpenXR. It also adds a package registry, Addressables, an audio mixer, multiplayer and localization.</p></div></li>
  <li><time>2026</time><div><h3>GameCraft 0.2</h3><p>Physics joints, a character controller, 2D physics, skeletal animation, glTF, OBJ and FBX import, terrain, navigation, packages and a profiler.</p></div></li>
  <li><time>2026</time><div><h3>GameCraft 0.1</h3><p>The first version: the engine, the editor, C# scripting and game export.</p></div></li>
</ul></div></section>
""")

# ---------------------------------------------------------------- faq
FAQ = [
    ("Is GameCraft free?", "Yes. GameCraft is released under the MIT License. You can use it for commercial games without paying royalties or fees."),
    ("Do I need an account or an internet connection?", "No. GameCraft runs entirely on your computer and does not collect usage data."),
    ("Can I open my Unity project?", "You can import it. Scenes, prefabs, materials, animations, animator controllers, ScriptableObjects and <code>.unitypackage</code> files are converted to GameCraft assets, and an import report lists anything that could not be converted."),
    ("Will my Unity scripts work?", "Scripts that use the supported parts of the UnityEngine API compile without changes. Scripts that use unsupported features fail to compile with an error naming the missing member. See <a href=\"unity.html\">Coming from Unity</a>."),
    ("Do Asset Store extensions work?", "Editor tools distributed as C# source and built with custom inspectors, editor windows, menu items or property drawers usually work. Most large extensions are distributed as compiled DLLs or use UI Toolkit, and these are not supported."),
    ("How are libraries and plugins loaded?", "All scripts in your Assets folder are compiled into one assembly, and scripts in Editor folders into a second one. Packages are folders containing C# source and a <code>package.json</code> file. They are installed from a local folder or a registry after you review the permissions they request. Compiled <code>.dll</code> files and native libraries are not loaded."),
    ("Is GameCraft ready for a commercial game?", "It is suitable for prototypes, game jams and small to medium projects. It is still in alpha: console export is not available, there is no asset marketplace, and no commercial games have shipped with it yet. Read the <a href=\"{{BLOB}}/docs/LIMITATIONS.md\">limitations</a> before starting a large project."),
    ("Will GameCraft support consoles?", "Console development kits are only available to developers accepted into each manufacturer's programme, and console code cannot be published openly. Support would be developed separately once access is granted. Xbox is the most likely first target."),
    ("Is it safe to open projects from other people?", "Treat a project like any other program. Its scripts and packages run with the same permissions as the editor."),
    ("Is GameCraft related to Unity?", "No. GameCraft is an independent project. It contains no Unity code or assets; it reads Unity's file formats and implements a compatible scripting API."),
]
page("faq.html", "FAQ - GameCraft", "Frequently asked questions about GameCraft.",
     header("Frequently asked questions", "If your question is not answered here, ask it in the <a href=\"{{REPO}}/issues\">issue tracker</a>.") +
     '<section class="section"><div class="wrap prose faq">' +
     "".join("<h3>%s</h3><p>%s</p>" % qa for qa in FAQ) + "</div></section>")

# ---------------------------------------------------------------- about
page("about.html", "About - GameCraft", "About GameCraft and LassarLabs.",
     header("About", "GameCraft is developed by LassarLabs and released as open source.") + """
<section class="section"><div class="wrap prose">
  <h2>Our approach</h2>
  <p>We think the tools people use to make games should work offline, store projects in open formats, and be free to inspect and change. GameCraft has no accounts, no telemetry and no license server.</p>
  <p>Features are covered by automated tests, and the ones that are incomplete are documented in the repository. The test suite covers the engine, the editor and the platforms it exports to.</p>
  <h2>Contributing</h2>
  <p>Bug reports, feature requests and pull requests are welcome on <a href="{{REPO}}">GitHub</a>. Before opening a pull request, run <code>tools/quality-gates.sh</code> and add a test for the behaviour you changed.</p>
  <h2>License</h2>
  <p>GameCraft is released under the <a href="{{BLOB}}/LICENSE">MIT License</a>. Third-party components and their licenses are listed in <a href="{{BLOB}}/docs/THIRD_PARTY_LICENSES.md">THIRD_PARTY_LICENSES.md</a>.</p>
</div></section>
""")

print("built", len(list(ROOT.glob("*.html"))), "pages")
