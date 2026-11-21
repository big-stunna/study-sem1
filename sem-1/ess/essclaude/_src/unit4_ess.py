import sys
from esslib import *
s = Story(); FIGN = [0]
def F(name, cap, mw=15.5, mh=9.2):
    FIGN[0] += 1; return FIG(f'img/{name}', f'Figure 4.{FIGN[0]} — {cap} (from the teacher\'s slides)', mw, mh)
def FR(pairs, mw=7.6, mh=5.4):
    items = []
    for name, cap in pairs:
        FIGN[0] += 1; items.append((f'img/{name}', f'Figure 4.{FIGN[0]} — {cap}'))
    return FIGROW(items, mw, mh)

s += BOX('HOW TO USE THIS GUIDE', ['Every topic of the unit is covered in simple language, with the figures and photos from your teacher\'s slides next to the topic they explain.',
        'Practice questions after each topic are tagged <b>[ EASY ]</b> (recall), <b>[ MEDIUM ]</b> (explain, compare) and <b>[ HARD ]</b> (numericals and multi-step), each with a full answer. Every value assumed in a numerical is stated in the question.'])
s += F('u4_s1_image8.jpeg', 'Sustainability: principles and systems — the four themes of this unit', 12.5, 6.2)

# ============================================================ 1
s += H1('1. Principle of the 4R\'s')
s += [P('The <b>4R principle</b> is a simple rule for using resources responsibly: <b>Reduce, Reuse, Recycle and Recover</b>. The earlier an "R" is applied, the more resources, energy and money are saved, so the order matters: reduce first, recover last.')]
s += TABLE([['R', 'Meaning', 'Examples from the slides'],
            ['<b>Reduce</b>', 'Use less. Limit energy use and only do what is really necessary. Keep the resource criteria to a minimum and use non-renewable resources responsibly.', 'Choose paper bags over polythene bags whenever possible.'],
            ['<b>Reuse</b>', 'Use the same item again instead of throwing it away; gradually replace single-use items with reusable ones.', 'Reusable mugs and water bottles; reuse packing (pallets, drums, bubble wrap, packaging peanuts); reuse shipping boxes and cartons; refill printer cartridges; reusing plastic bags to make attractive items.'],
            ['<b>Recycle</b>', 'Convert waste into new material. Anything that can be recycled chemically should be, because it can be turned back into new materials.', 'Recycle paper, plastic, metal and glass; compost food scraps or give them as fertiliser to a nearby farm; recycle damaged clothing; recycle electronics (e-waste); plastic materials.'],
            ['<b>Recover</b>', 'If waste is left after reuse and recycling, get the energy out of it, for example in a <b>waste-to-energy plant</b>. This is called recovery.', 'Waste-to-energy plant producing energy from the leftover waste.']], [0.9, 3, 3.1])
s += KEY('Waste hierarchy (best to worst): <b>Reduce → Reuse → Recycle → Recover → Landfill</b>. Landfill is what remains after all four R\'s have been used.')
s += RECALL(['4R = Reduce, Reuse, Recycle, Recover.', 'Reduce: use less (paper bags over polythene); Reuse: use again (bottles, cartons); Recycle: make new material (paper, plastic, metal, glass, compost); Recover: waste-to-energy.'])
s += QA('e', 'What are the four R\'s? Give one example for each.', [('lines', ['Reduce — use paper bags instead of polythene bags', 'Reuse — refill printer cartridges / use reusable water bottles', 'Recycle — recycle paper, plastic, metal and glass, or compost food scraps', 'Recover — burn leftover waste in a waste-to-energy plant to generate energy'])])
s += QA('m', 'Distinguish between reuse and recycle.', 'Reuse means using the same item again in the same or another way without changing it (a refilled cartridge, a water bottle). Recycle means processing the waste material to make new material or products (plastic into new plastic items, food scraps into compost). Reuse needs less energy because the item is not reprocessed.')
s += QA('h', 'A town produces 10 tonnes of solid waste per day. Reduction measures avoid 15% of it. Of the remaining waste, 30% is recycled, 20% is composted (counted as recycling) and 25% goes to a waste-to-energy plant; the rest is landfilled. How much goes to landfill each day?',
        [('work', '''
Waste after reduction = 10 x (1 - 0.15)        = 8.5 t/day
Recycled              = 0.30 x 8.5             = 2.55 t
Composted             = 0.20 x 8.5             = 1.70 t
Recovered (energy)    = 0.25 x 8.5             = 2.125 t
Total diverted        = 2.55 + 1.70 + 2.125    = 6.375 t
Landfill              = 8.5 - 6.375            = 2.125 t/day
'''), 'About <b>2.1 tonnes per day (25% of the remaining waste, 21% of the original 10 t)</b> still goes to landfill. 7.9 t of the original 10 t is kept out of landfill.'])

# ============================================================ 2
s += H1('2. Renewable Energy')
s += [P('<b>Renewable energy</b> comes from natural sources such as the sun, wind, biomass and water, which are <b>naturally replenished</b>. It is also called <b>green</b> or <b>clean</b> energy because generating it releases no or hardly any greenhouse gases, unlike fossil fuels such as coal and oil. Moving away from fossil fuels is a key step in fighting climate change, and choosing renewable electricity and heating for your home reduces your carbon footprint and can lower your energy costs.')]
s += TABLE([['Source', 'How it gives energy (short note)'], ['Solar energy', 'Sunlight converted to electricity by photovoltaic (PV) panels or to heat by collectors'], ['Wind energy', 'Moving air turns turbine blades connected to a generator'], ['Geothermal energy', 'Heat from inside the Earth gives steam or hot water'], ['Hydropower', 'Falling or flowing water turns turbines'], ['Ocean energy', 'Tides, waves and ocean temperature differences'], ['Bio-energy', 'Fuel or electricity from biomass such as crop residue, wood and organic waste']], [1.4, 5])
s += TABLE([['Renewable', 'Non-renewable (fossil fuels)'], ['Naturally replenished', 'Take millions of years to form; get used up'], ['No or very low GHG emissions in operation', 'Release CO<sub>2</sub> and other pollutants when burned'], ['Often available locally; improves energy security', 'Often imported; price depends on world markets'], ['Output can vary (sun, wind) so storage and grid support are needed', 'Steady, on-demand output']], [1, 1])
s += H2('2.1 Initiatives shaping India\'s transition to renewable energy')
s += TABLE([['Initiative', 'Launched / by', 'What it is and its objectives'],
            ['<b>PM-KUSUM</b> (Pradhan Mantri Kisan Urja Suraksha evam Utthaan Mahabhiyan)', 'March 2019, Ministry of New and Renewable Energy (MNRE)', 'Promotes solar energy in agriculture. <b>De-dieselisation</b> (solar pumps replace diesel irrigation pumps); <b>income enhancement</b> (farmers sell surplus solar power to the grid); <b>energy security</b> for farming; <b>environmental benefit</b> (lower carbon emissions).'],
            ['<b>PLI scheme</b> (Production Linked Incentive) for High-Efficiency Solar PV Modules', 'Government of India', 'Builds GW-scale manufacturing of high-efficiency solar modules and an ecosystem for local sourcing; reduces import dependence. Objectives: build capacity; bring cutting-edge technology (technology-agnostic, but better-performing technologies are rewarded); integrated plants for quality and competitiveness; local material sourcing; employment and technological self-sufficiency.'],
            ['<b>Green Energy Corridor (GEC)</b>', '2015, Government of India', 'Integrates solar and wind power into the national grid by transmitting it from remote generation sites to consumption centres. Objectives: transmission lines and substations; <b>grid stability</b> against the variability and intermittency of renewables; support India\'s target of <b>500 GW</b> of non-fossil capacity by <b>2030</b>; jobs and growth.'],
            ['<b>FAME</b> (Faster Adoption and Manufacturing of (Hybrid &amp;) Electric Vehicles)', '2015, under the National Electric Mobility Mission Plan (NEMMP)', 'Promotes electric and hybrid vehicles to cut fossil-fuel dependence and vehicle emissions. <b>Phase I (2015–2019):</b> initial demand through subsidies, pilot projects and charging infrastructure; about 2.8 lakh EVs. <b>Phase II (2019–2024):</b> ₹10,000 crore budget, mainly for public transport (e-buses, e-3-wheelers, e-2-wheelers) and nationwide charging. <b>FAME III</b> (proposed after 2024): private electric four-wheelers, rural charging, domestic EV and battery manufacturing.'],
            ['<b>National Offshore Wind Energy Policy</b>', '2015, Government of India', 'Uses India\'s Exclusive Economic Zone (up to 200 nautical miles). Objectives: promote offshore wind farms including through PPPs; attract investment in energy infrastructure; spatial planning of maritime renewable resources; energy security and emission reduction; indigenisation and R&amp;D; skilled jobs.']], [1.6, 1.4, 4.2])
s += RECALL(['Renewable = naturally replenished (solar, wind, geothermal, hydro, ocean, bio-energy); almost no GHG emissions.', 'PM-KUSUM (2019, MNRE): solar for farmers. PLI: solar module manufacturing. GEC (2015): grid for renewables, 500 GW non-fossil by 2030.', 'FAME (2015): EVs, Phase I 2015–19 (≈ 2.8 lakh EVs), Phase II 2019–24 (₹10,000 crore). Offshore Wind Policy (2015): EEZ up to 200 nautical miles.'])
s += QA('e', 'Define renewable energy and name four sources.', 'Renewable energy is energy generated from natural sources that are naturally replenished, with no or very little greenhouse gas emission. Examples: solar, wind, hydropower, geothermal, ocean and bio-energy.')
s += QA('m', 'State the four objectives of PM-KUSUM.', [('steps', ['De-dieselisation of agriculture: replace diesel irrigation pumps with solar pumps.', 'Income enhancement: farmers can sell surplus solar power to the grid.', 'Energy security: reliable, sustainable energy for farming.', 'Environmental benefits: lower carbon emissions and use of clean energy.'])])
s += QA('m', 'Why does India need the Green Energy Corridor?', [('steps', ['Renewable plants (solar, wind) are often far from cities, where power is used.', 'Dedicated transmission lines and substations are needed to carry that power to the grid.', 'The grid must also cope with the ups and downs (intermittency) of renewable output.', 'This helps India reach 500 GW of non-fossil capacity by 2030.'])])
s += QA('h', 'A farmer\'s diesel pump burns 1.5 litres of diesel per hour and runs 6 hours a day for 150 days a year. Diesel costs ₹90 per litre and each litre releases 2.68 kg CO<sub>2</sub>. (a) Find the yearly diesel use, cost and CO<sub>2</sub>. (b) A solar pump costing ₹1,80,000 replaces it with negligible running cost: find the simple payback time.',
        [('work', '''
(a) Hours per year = 6 h x 150 days       = 900 h
    Diesel used    = 1.5 L/h x 900 h      = 1350 L
    Cost           = 1350 L x Rs 90       = Rs 1,21,500
    CO2            = 1350 L x 2.68 kg/L   = 3618 kg  (about 3.6 tonnes)
(b) Payback = 1,80,000 / 1,21,500 = 1.48 years (about 18 months)
'''), 'The solar pump saves <b>₹1.2 lakh and 3.6 t of CO<sub>2</sub> per year</b> and pays for itself in about <b>1.5 years</b>. (Government subsidy under PM-KUSUM would shorten this further.)'])
s += QA('h', 'India aims for 500 GW of non-fossil capacity by 2030. Assume 200 GW were installed at the start of 2024. What average capacity must be added per year during 2024–2030 (7 years)? Also, if FAME-I put 2.8 lakh EVs on the road and each avoids 1.5 tonnes of CO<sub>2</sub> a year (assumed), what is the yearly saving?',
        [('work', '''
Capacity to add = 500 - 200       = 300 GW
Per year        = 300 / 7         = 42.9 GW per year
EV saving       = 2,80,000 x 1.5  = 4,20,000 tonnes CO2 per year (4.2 lakh t)
'''), 'About <b>43 GW per year</b> must be added, and the FAME-I vehicles avoid roughly <b>4.2 lakh tonnes of CO<sub>2</sub> per year</b> under the assumption given.'])

# ============================================================ 3
s += H1('3. Nature-Based Solutions (NBS)')
s += [P('<b>Nature-based solutions</b> are the sustainable management and use of nature to tackle social and environmental challenges. The International Union for Conservation of Nature (<b>IUCN</b>) defines NBS as <b>actions to protect, sustainably manage and restore natural and modified ecosystems</b> that address societal challenges effectively and adaptively, while providing human well-being and biodiversity benefits.')]
s += BUL(['NBS creates harmony between people and nature, enables ecological development and is a holistic, people-centred response to climate change.', 'NBS is an essential part of the global effort to meet the goals of the <b>Paris Agreement</b> on climate change.', 'It helps local people deal with climate impacts, improves ecosystem services and stores carbon.'])
s += TABLE([['Use of NBS', 'Meaning', 'Examples'],
            ['<b>Ecosystem restoration</b>', 'Any degraded ecosystem can be improved by restoration', 'Agricultural areas, savannah, wetlands, protected reserves, fisheries, managed plantations, riversides, coastal areas'],
            ['<b>Addressing urban issues</b>', 'NBS combined with man-made infrastructure benefits human health and urban biodiversity', 'Green roofs and green walls, permeable pavements (extra: urban parks, rain gardens)'],
            ['<b>Disaster risk reduction</b>', 'Climate change increases the frequency and intensity of hazards; NBS helps communities prepare for, cope with and recover from disasters', '(Extra: mangroves and coral reefs against storm surges, wetlands and floodplains against floods)']], [1.6, 2.8, 2.6])
s += RECALL(['NBS = protect, sustainably manage and restore ecosystems to solve societal problems (IUCN definition).', 'Three uses: ecosystem restoration, urban issues (green roofs and walls, permeable pavements), disaster risk reduction.', 'Supports the Paris Agreement; stores carbon.'])
s += QA('e', 'Who defines nature-based solutions and what does the term mean?', 'The IUCN defines nature-based solutions as actions to protect, sustainably manage and restore natural and modified ecosystems so that they address societal challenges effectively while giving human well-being and biodiversity benefits.')
s += QA('m', 'Explain how nature-based solutions help in cities. Give two examples.', 'NBS is combined with man-made infrastructure to improve human health and urban biodiversity. Examples: green roofs and green walls (cooling, insulation, habitat) and permeable pavements (let rainwater soak into the ground, reducing flooding).')
s += QA('m', 'How can NBS reduce disaster risk?', 'Climate change increases the frequency, intensity and magnitude of hazards. Healthy natural systems act as buffers (for example wetlands absorbing flood water, mangroves reducing storm waves), so NBS helps communities to prepare for, cope with and recover from disasters.')

# ============================================================ 4
s += H1('4. Green Buildings')
s += [P('A <b>green building</b> (also called green construction or sustainable building) adds environmental care to the usual design concerns of economy, utility, durability and comfort. Compared with a conventional building it <b>uses less water, optimises energy efficiency, conserves natural resources, generates less waste and provides healthier space for its occupants</b>. Green buildings are designed to reduce the overall impact on human health and the natural environment by using energy, water and other resources efficiently and by reducing waste, pollution and environmental degradation.')]
s += F('u4_s13_image9.png', 'Features of a green building: solar panels, shading, insulation, low-flow fixtures, rain-water collection', 11.5, 6.8)
s += H2('4.1 Concept of green buildings')
s += BUL(['Sustainable site planning', 'Building design optimisation', 'Energy performance optimisation', 'Renewable energy utilisation', 'Water and waste management', 'Solid waste management', 'Sustainable building materials and construction technology', 'Health, well-being and environmental quality'])
s += F('u4_s14_image10.png', 'Conceptual drawing of a green building', 12.5, 6.5)
s += H2('4.2 Green building rating systems')
s += [P('A <b>rating system</b> is an evaluation tool that measures the environmental performance of a building through its life cycle. It has a set of criteria for the design, construction and operation of the building. Each criterion has pre-assigned points and benchmarks that are largely measurable. A project is awarded points when it meets the criteria; the points are added up and decide its final rating. Rating systems are mostly voluntary and have helped to spread awareness of green building design.')]
s += TABLE([['System', 'Full name', 'Origin'], ['BREEAM', 'Building Research Establishment\'s Environmental Assessment Method', 'UK, 1990'], ['GBTool', 'Developed by the International Framework Committee for the Green Building Challenge (more than 25 countries)', 'International, since 1998'], ['LEED', 'Leadership in Energy and Environmental Design', 'USA, 1998'], ['CASBEE', 'Comprehensive Assessment System for Building Environmental Efficiency', 'Japan, 2001'], ['IGBC', 'Indian Green Building Council', 'India, formed 2001']], [1, 3.5, 2])
s += P('<b>LEED levels</b> (from the slide): Certified 40–49 points, Silver 50–59, Gold 60–79, Platinum 80 and above.')
s += F('u4_s17_image11.png', 'LEED rating scale', 11, 6.5)
s += H2('4.3 Fundamental principles of green buildings')
s += TABLE([['Principle', 'Idea'], ['Structural design efficiency', 'Has the largest effect on cost and performance; aims to minimise environmental impact over all life-cycle stages'], ['Energy efficiency', 'Plan the layout to let in natural light and warmth; shade the roof with trees as an eco-friendly alternative to air conditioning'], ['Water efficiency', 'Use water that has been collected, used, purified and reused to minimise consumption'], ['Material efficiency', 'Use materials that can be recycled and that save energy; e.g. solar panels give light and are an energy source'], ['Waste and toxic reduction', 'Reuse resources; what is waste for one process can be useful for another']], [1.6, 4.9])
s += H2('4.4 Case studies from the slides')
s += FR([('u4_s19_image12.png', 'One Central Park, Sydney, Australia'), ('u4_s20_image13.png', 'Bahrain World Trade Center, Bahrain')])
s += FR([('u4_s21_image14.png', 'Vancouver Convention Centre West, Canada'), ('u4_s22_image15.png', 'Suzlon One Earth, Pune, India')])
s += FR([('u4_s23_image16.png', 'ACROS Fukuoka Prefectural International Hall, Japan')], 8.5, 6)
s += TABLE([['Building', 'Green feature to remember (short note)'], ['One Central Park, Sydney', 'Vertical gardens and green walls covering the towers; brings plants into a dense city'], ['Bahrain World Trade Center', 'Wind turbines built between the twin towers generate part of the building\'s power'], ['Vancouver Convention Centre West', 'Large living (green) roof; waterfront site with energy- and water-saving systems'], ['Suzlon One Earth, Pune', 'Campus designed for energy and water efficiency using solar and wind; a leading Indian green campus'], ['ACROS Fukuoka', 'Stepped, planted terraces that form a park on the building and cool it']], [2, 4.5])
s += [P('<i>The slides give only the names and photos of these buildings; the notes above are short general details, so keep the main point (what makes each one green) for the exam.</i>')]
s += RECALL(['Green building: less water and energy, less waste, healthier occupants.', 'Rating systems: BREEAM (UK 1990), GBTool (since 1998), LEED (US 1998), CASBEE (Japan 2001), IGBC (India 2001).', 'LEED: 40–49 Certified, 50–59 Silver, 60–79 Gold, 80+ Platinum.', 'Principles: structural, energy, water, material efficiency; waste and toxic reduction.'])
s += QA('e', 'What is a green building?', 'A building that uses less water, optimises energy efficiency, conserves natural resources, generates less waste and gives a healthier space for occupants than a conventional building.')
s += QA('e', 'Name any four green building rating systems and the country of origin of each.', [('lines', ['BREEAM — United Kingdom (1990)', 'LEED — United States (1998)', 'CASBEE — Japan (2001)', 'IGBC — India (formed 2001)'])])
s += QA('m', 'Explain how a green building rating system works.', [('steps', ['A set of criteria covers design, construction and operation of the building.', 'Each criterion carries pre-assigned points with quantifiable benchmarks.', 'The project earns points for every criterion it meets.', 'Points are added up and the total decides the final rating (for LEED: Certified, Silver, Gold or Platinum).'])])
s += QA('h', 'Projects A, B, C and D score 38, 48, 72 and 85 points on the LEED scale. Give the rating of each. A new 20,000 m² building is designed to use 90 kWh/m²/year instead of 150 kWh/m²/year; with 0.8 kg CO<sub>2</sub> per kWh and electricity at ₹8 per kWh, find the yearly saving in energy, CO<sub>2</sub> and money.',
        [('work', '''
Ratings: A = 38 points -> below 40, not certified
         B = 48 points -> Certified (40-49)
         C = 72 points -> Gold      (60-79)
         D = 85 points -> Platinum  (80 and above)
Energy saved = (150 - 90) x 20,000 = 60 x 20,000 = 12,00,000 kWh per year
CO2 avoided  = 12,00,000 x 0.8     = 9,60,000 kg = 960 tonnes per year
Money saved  = 12,00,000 x Rs 8    = Rs 96,00,000 (Rs 96 lakh) per year
'''), 'The design saves <b>12 lakh kWh, 960 t CO<sub>2</sub> and ₹96 lakh each year</b> (a 40% reduction in energy use).'])

# ============================================================ 5
s += H1('5. Sustainable Cities')
s += [P('A <b>sustainable city</b> is an urban area designed to be <b>environmentally friendly, economically viable and socially inclusive</b>. The idea is to balance urban growth with the natural environment, so that natural resources are managed responsibly and the needs of present and future generations are met. Renewable energy, efficient public transport, waste reduction and smart urban planning are combined to cut the city\'s ecological footprint and give residents a high quality of life.')]
s += H2('5.1 Key features')
s += TABLE([['Feature', 'Elements'],
            ['<b>1. Green infrastructure and urban planning</b>', '<b>Green spaces and parks</b> (community gardens, urban forests) improve air quality and reduce urban heat islands; <b>smart zoning</b> (mixed-use residential, commercial and recreational areas) encourages walking; <b>eco-friendly architecture</b> (energy-efficient design, recycled materials, green roofs and walls)'],
            ['<b>2. Renewable energy and energy efficiency</b>', 'Clean energy sources (solar, wind, geothermal) reduce reliance on fossil fuels; smart grids, LED street lighting and energy-saving technologies cut consumption'],
            ['<b>3. Sustainable transportation</b>', 'Efficient public transit lowers congestion and GHGs; cycling and pedestrian infrastructure and car-free zones promote healthy lifestyles; electric and hybrid vehicles keep the air clean'],
            ['<b>4. Waste and water management</b>', 'Recycling and composting programmes reduce landfill; water conservation through rain-water harvesting, greywater recycling and sustainable drainage'],
            ['<b>5. Smart technology and data-driven governance</b>', 'Internet of Things (IoT) sensors and real-time monitoring improve traffic, energy use and public safety; data analytics optimises resource allocation and planning']], [2, 4.7])
s += H2('5.2 Challenges')
s += TABLE([['Challenge', 'Why it is hard'], ['1. High initial investment', 'Green infrastructure, renewable projects and modern public transport need large upfront funds, difficult for cities with small budgets'],
            ['2. Policy and regulatory barriers', 'Supportive policy is essential, but bureaucracy, outdated planning practices and conflicting stakeholder interests slow progress'],
            ['3. Technological integration', 'Smart-city solutions need strong technology infrastructure and expertise; fitting new systems into existing ones is complex and may meet resistance'],
            ['4. Social and cultural challenges', 'Changing habits and mindsets; public resistance, low awareness, weak community engagement'],
            ['5. Legacy infrastructure', 'Ageing buildings and transport networks were not designed for modern sustainable technology; retrofitting is costly and time-consuming']], [1.8, 4.9])
s += P('<b>Examples of sustainable cities</b> (from the slide): Copenhagen (Denmark), Amsterdam (Netherlands) and Singapore. <i>Extra detail:</i> Copenhagen and Amsterdam are known for cycling networks and Singapore for green buildings, urban greenery and water recycling.')
s += RECALL(['Sustainable city: environmentally friendly + economically viable + socially inclusive.', 'Features: green infrastructure, renewable energy and efficiency, sustainable transport, waste and water management, smart technology.', 'Challenges: investment, policy, technology integration, social and cultural change, legacy infrastructure.'])
s += QA('e', 'Define a sustainable city.', 'An urban area designed to be environmentally friendly, economically viable and socially inclusive, balancing growth with nature so that resources are used responsibly for present and future generations.')
s += QA('m', 'Explain any three features of a sustainable city.', [('lines', ['<b>Green infrastructure:</b> parks and urban forests improve air quality and reduce urban heat islands; mixed-use zoning reduces car dependence.', '<b>Sustainable transport:</b> public transit, cycle lanes and electric vehicles cut congestion and GHG emissions.', '<b>Waste and water management:</b> recycling, composting, rain-water harvesting and greywater recycling reduce landfill and save water.'])])
s += QA('m', 'Why is legacy infrastructure a challenge for sustainable cities?', 'Old buildings and transport networks were not designed for modern sustainable technology. Retrofitting them to even today\'s standards is costly and slow, and reaching a truly sustainable level is harder still.')
s += QA('h', 'A city replaces 50,000 street lights of 150 W with LED lights of 70 W. They burn 11 hours a day, 365 days a year. Electricity costs ₹8 per kWh and emits 0.8 kg CO<sub>2</sub> per kWh. The project costs ₹60 crore. Find the yearly saving in energy, money and CO<sub>2</sub>, and the payback time.',
        [('work', '''
Power saved per light = 150 - 70 = 80 W
Total power saved     = 80 W x 50,000 = 4,000,000 W = 4000 kW
Hours per year        = 11 x 365 = 4015 h
Energy saved          = 4000 kW x 4015 h = 1,60,60,000 kWh (1.606 crore kWh)
Money saved           = 1,60,60,000 x Rs 8 = Rs 12,84,80,000 = Rs 12.85 crore
CO2 avoided           = 1,60,60,000 x 0.8 = 1,28,48,000 kg = 12,848 tonnes
Payback               = Rs 60 crore / Rs 12.85 crore per year = 4.7 years
'''), 'The project saves <b>1.6 crore kWh, ₹12.85 crore and about 12,850 t of CO<sub>2</sub> a year</b> and pays back in about <b>4.7 years</b> (even faster if the lights also need less maintenance).'])

# ============================================================ 6
s += H1('6. Life Cycle Thinking')
s += [P('<b>Life Cycle Thinking (LCT)</b> means looking beyond the production site and the manufacturing process and including the <b>environmental, social and economic impacts of a product over its whole life cycle</b>. Its main goals are to reduce the product\'s use of resources and emissions to the environment and to improve its socio-economic performance across its life. It links the economic, social and environmental dimensions within an organisation and along the whole value chain.')]
s += [P('A product\'s life cycle can begin with the <b>extraction of raw materials</b> from natural resources and the generation of energy. Materials and energy then go into <b>production, packaging, distribution, use and maintenance</b>, and finally into <b>recycling, reuse, recovery or final disposal</b>.')]
s += F('u4_s29_image17.png', 'The product life cycle: from extraction to disposal, with recycling, reuse and recovery loops', 9.5, 8)
s += H2('6.1 Life cycle assessment (LCA)')
s += [P('<b>LCA</b> is an internationally standardised method. It <b>quantifies all relevant emissions and resources consumed</b>, and the related environmental and health impacts and resource depletion, for any good or service, from the extraction of resources through production, use and recycling to the disposal of the remaining waste.')]
s += BUL(['Life cycle approaches can be used in <b>all sectors</b> and can examine key impact categories: environmental LCA, social LCA, carbon footprint, water footprint and others, and their effect on all three pillars of sustainability (life cycle sustainability assessment).',
          'LCT is the conceptual base that has moved the sustainability agenda forward in public and private sectors, supporting decisions on policy, product development, production, procurement and final disposal.'])
s += F('u4_s32_image18.png', 'Life cycle stages: each stage needs labour, energy and materials and releases emissions to land, air and water, and has social impacts', 14, 6.8)
s += H2('6.2 Benefits of life cycle approaches')
s += BUL(['<b>At the macro level:</b> they avoid shifting a problem from one life-cycle stage to another, from one place to another, or from one medium (air) to another (water or land).',
          '<b>At the micro level:</b> product designers, service providers and government agents can make long-term choices considering air, water and land together.',
          'Better <b>image and brand value</b> for large and small producers who adopt life cycle and sustainability management.',
          'Governments can show <b>global responsibility and governance</b> by supporting programmes and sharing sustainability options worldwide.',
          'They give consumers <b>better information</b> for choosing products, transport and energy sources, steering consumption in a more sustainable direction.'])
s += RECALL(['LCT: consider environmental, social and economic impacts over the whole life cycle.', 'Stages: extraction → production → packaging → distribution → use and maintenance → recycling / reuse / recovery / disposal.', 'LCA: standardised method that quantifies emissions and resources for a product or service over its life cycle.', 'Benefit: avoids shifting problems between stages, places and media; better information for consumers.'])
s += QA('e', 'What is Life Cycle Thinking?', 'Looking at the environmental, social and economic impacts of a product over its entire life cycle, from raw-material extraction to final disposal, and not only at the production site.')
s += QA('m', 'List the stages in the life cycle of a product.', [('steps', ['Extraction of raw materials and energy generation', 'Production (manufacture)', 'Packaging and distribution', 'Use and maintenance', 'Recycling, reuse, recovery or final disposal'])])
s += QA('m', 'What does "avoid shifting problems" mean in a life cycle approach?', 'A fix that solves a problem at one stage can create a bigger one elsewhere — for example cleaning a factory\'s exhaust but sending the waste to land, or making a product use less energy in the factory but much more in use. Looking at the whole life cycle shows these trade-offs, so problems are not just moved from one stage, place or medium (air, water, land) to another.')
s += QA('h', 'LCA of a product gives these emissions per unit: extraction 12 kg CO<sub>2</sub>e, manufacture 30, packaging and distribution 8, use 45, end of life 5. (a) Find the total and the percentage share of each stage. (b) Which stage is the "hotspot"? (c) If the use-phase energy is halved by a better design, what is the new total and the percentage reduction?',
        [('work', '''
Total = 12 + 30 + 8 + 45 + 5 = 100 kg CO2e
Share : extraction 12%, manufacture 30%, packaging/distribution 8%,
        use 45%, end of life 5%
Hotspot = use stage (45%)
Use halved : 45 / 2 = 22.5 kg
New total  = 12 + 30 + 8 + 22.5 + 5 = 77.5 kg CO2e
Reduction  = (100 - 77.5) / 100 = 22.5%
'''), 'The <b>use stage</b> is the hotspot, so improving it gives the biggest gain: the total falls from 100 to <b>77.5 kg CO<sub>2</sub>e (22.5% lower)</b>.'])

ok = build('/home/sleepy/STUDY:)/sem-1/ess/essclaude/ESS_Unit4_StudyGuide.pdf' if len(sys.argv) < 2 else sys.argv[1], 4, 'Sustainability and Engineering Solutions',
           'This guide covers every topic of the unit as the teacher\'s slides present it, in simple language, with the slide figures and photos included. Try each tagged question before reading its answer.', s)
print('BUILD OK' if ok else 'BUILD HAS PROBLEMS')
