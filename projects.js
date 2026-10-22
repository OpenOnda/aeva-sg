/* Design concepts: what AEVA can design and build.
   Images: images/projects/<slug>-1.jpg, -2.jpg, -3.jpg (generated in Midjourney, see the prompt sheet).
   Each concept renders at design.html?d=<slug>. */
const PROJECTS = [
  {
    slug: "treehouse-loft",
    title: "The Treehouse Loft",
    space: "Shared kids' bedroom",
    suits: "HDB BTO & resale",
    style: "White oak, warm strip light",
    build: "3 to 5 weeks",
    tags: ["kids", "hdb", "carpentry"],
    summary: "For siblings sharing a small room. We build up instead of out.",
    story: "A white oak loft bed with a sleeping deck above and a cosy den below, joined by a short ladder with wide, rounded rungs. A wall of shallow cubbies runs alongside the ladder so every toy has a home at kid height. Warm 2700K strip lights tucked under the deck make the den glow at story time without lighting up the whole room.",
    scope: ["Loft bed with play den", "Cubby storage wall", "Under-deck strip lighting", "Rounded edges throughout"]
  },
  {
    slug: "reading-nook-house",
    title: "The Reading Nook",
    space: "Living room & library wall",
    suits: "HDB, condo & landed",
    style: "Light oak, linen, cove light",
    build: "3 to 4 weeks",
    tags: ["kids", "hdb", "condo", "carpentry"],
    summary: "Built around one idea: a family that reads together.",
    story: "A bay window turned into a deep cushioned window seat, framed by floor-to-ceiling oak shelves. The lowest two rows are kept for picture books little ones can reach themselves. Cove lighting along the shelf tops gives the whole wall a soft evening glow, so it becomes the place everyone drifts to after dinner.",
    scope: ["Window seat with storage", "Floor-to-ceiling library wall", "Cove lighting", "Kid-height book shelves"]
  },
  {
    slug: "little-forest-nursery",
    title: "Little Forest Nursery",
    space: "Nursery",
    suits: "First homes & BTOs",
    style: "Sage plaster, solid wood",
    build: "2 to 4 weeks",
    tags: ["kids", "hdb", "carpentry"],
    summary: "A nursery designed to grow up in stages.",
    story: "A solid wood cot that converts into a toddler bed, a changing station that later becomes a study desk, and a sage-green plaster wall with a rounded timber arch. Every switch is dimmable, so late-night feeds happen under a low amber glow instead of the ceiling lamp.",
    scope: ["Convertible cot", "Changing table to study desk", "Timber arch feature wall", "Dimmable lighting plan"]
  },
  {
    slug: "walnut-and-warmth",
    title: "Walnut & Warmth",
    space: "Living room",
    suits: "HDB, condo & landed",
    style: "Fluted walnut, concealed LED",
    build: "4 to 6 weeks",
    tags: ["hdb", "condo", "landed", "carpentry"],
    summary: "The cosiness of an old library, without losing the light.",
    story: "Walnut veneer for a floating TV console and a fluted feature wall, paired with oak flooring and linen curtains. Concealed LED profiles above the console and along the ceiling edge do most of the lighting work after dark, so the room glows instead of glares.",
    scope: ["Fluted walnut feature wall", "Floating TV console", "Ceiling cove lighting", "Hidden storage"]
  },
  {
    slug: "cabin-kitchen",
    title: "The Cabin Kitchen",
    space: "Open-concept kitchen",
    suits: "HDB, condo & landed",
    style: "Oak, quartz, pendant light",
    build: "5 to 7 weeks",
    tags: ["hdb", "condo", "landed", "carpentry"],
    summary: "An open kitchen where homework and dinner happen side by side.",
    story: "The kitchen wall comes down and an oak peninsula with a quartz top takes its place, so whoever is cooking can still see the kids at the counter. Full-height oak cabinets hide the mess, and a pair of open shelves shows off the good stuff. Warm glass pendants over the counter sit on their own dimmer, so the space shifts easily from cooking to winding down.",
    scope: ["Oak and quartz peninsula", "Full-height oak cabinets", "Open shelving with under-shelf light", "Pendant lighting on dimmer"]
  },
  {
    slug: "study-that-grows",
    title: "The Study That Grows",
    space: "Kids' study room",
    suits: "HDB, condo & landed",
    style: "Oak, pegboard, task light",
    build: "3 to 4 weeks",
    tags: ["kids", "hdb", "carpentry"],
    summary: "One study for several children, built to adjust as they grow.",
    story: "A long oak desk along the window with a zone for each child, each with adjustable shelf height and its own task lamp. Above it, a pegboard wall lets the kids change their layout every school term. Closed cabinets below keep school bags and art supplies out of sight, with a soft reading corner on the last wall.",
    scope: ["Multi-zone study desk", "Pegboard wall", "Individual task lighting", "Reading corner"]
  }
];
