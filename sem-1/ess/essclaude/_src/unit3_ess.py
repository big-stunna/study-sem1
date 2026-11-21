import sys
from esslib import *
I = lambda n: f'img/{n}'
s = Story()
FIGN = [0]
def F(name, cap, mw=15.5, mh=9.2):
    FIGN[0] += 1
    return FIG(I(name), f'Figure 3.{FIGN[0]} — {cap} (from the teacher\'s slides)', mw, mh)

s += BOX('HOW TO USE THIS GUIDE', ['Every topic in the unit is covered in simple language. The figures are the ones from your teacher\'s slides, placed next to the topic they explain.',
        'After each topic there are practice questions tagged <b>[ EASY ]</b> (definitions, recall), <b>[ MEDIUM ]</b> (explain, compare, apply) and <b>[ HARD ]</b> (numericals, multi-step reasoning), each with a full answer. Values assumed in a numerical are always stated in the question.'])
s += F('u3_poster.png', 'Unit 3 at a glance: climate change, carbon footprint, ozone and acid rain, SDGs, legislation, EIA', 14, 8.5)

# ================================================================= 1
s += H1('1. Climate Change')
s += H2('1.1 What it is')
s += [P('<b>Climate change</b> means long-term shifts in temperatures and weather patterns. Some shifts are natural, for example because the Sun\'s activity changes or because of large volcanic eruptions. But since the 1800s, <b>human activities have been the main driver</b>, mainly the burning of fossil fuels (coal, oil and gas).')]
s += [P('Burning fossil fuels releases greenhouse gases that blanket the Earth and trap the Sun\'s heat. This leads to <b>global warming</b> and climate change. The world is now warming faster than at any point in recorded history, and warmer temperatures disturb the usual balance of nature, which puts humans and all other forms of life at risk.')]
s += KEY('<b>Weather</b> is what the atmosphere is doing today in one place. <b>Climate</b> is the average pattern of weather over many years (usually 30 or more). Climate change is therefore a change in the long-term average, not a hot day or a single storm.')
s += H2('1.2 Causes of climate change')
s += TABLE([['Cause', 'How it adds greenhouse gases (GHGs)'],
            ['Generating power', 'Most electricity and heat still comes from burning coal, oil or gas, which releases carbon dioxide (CO<sub>2</sub>) and nitrous oxide (N<sub>2</sub>O). A little over a quarter of the world\'s electricity now comes from wind, solar and other renewables, which emit little or no GHGs.'],
            ['Manufacturing goods', 'Industry burns fossil fuels to make cement, iron, steel, electronics, plastics and clothes. Mining and construction also release gases, and plastics are made from fossil-fuel chemicals. Manufacturing is one of the largest sources of GHGs worldwide.'],
            ['Cutting down forests', 'Cut trees release the carbon they stored, and fewer forests means less CO<sub>2</sub> absorbed. About <b>12 million hectares</b> of forest are destroyed every year. Deforestation together with agriculture and other land-use change causes roughly <b>a quarter</b> of global GHG emissions.'],
            ['Using transportation', 'Cars, trucks, ships and planes mostly run on fossil fuels. Road vehicles are the largest part (petrol/gasoline in internal-combustion engines). Transport gives nearly <b>one quarter</b> of energy-related CO<sub>2</sub>, and ship and plane emissions keep growing.'],
            ['Producing food', 'CO<sub>2</sub>, methane (CH<sub>4</sub>) and other gases come from clearing land for farming and grazing, digestion in cows and sheep, fertilisers and manure, farm machinery and fishing boats running on fuel, and packaging and distribution.'],
            ['Powering buildings', 'Homes and commercial buildings use <b>over half</b> of all electricity. Rising air-conditioner ownership and more lighting, appliances and connected devices increase energy-related CO<sub>2</sub>.'],
            ['Consuming too much', 'Our energy use, travel, food and waste, and goods such as clothing, electronics and plastics all add GHGs. The richest 1% of people together emit more than the poorest 50%.']], [1.5, 5.2])
s += F('u3_p4.png', 'Fossil-fuel electricity and manufacturing versus renewable electricity', 13, 6.6)
s += F('u3_p8.png', 'Additional causes of climate change: deforestation, transport, food, buildings, consumption', 13, 6.6)
s += H2('1.3 Effects of climate change')
s += TABLE([['Effect', 'What happens'],
            ['Hotter temperature', 'Global surface temperature rises with GHG concentration. More heat-related illness, harder outdoor work, wildfires start easily and spread faster, and glaciers and ice caps melt.'],
            ['More severe storms', 'Warmer air holds more moisture, so extreme rain and floods increase. Cyclones, hurricanes and typhoons feed on warm ocean water, so they become more destructive.'],
            ['Increased drought', 'Water becomes scarcer in more regions: farm droughts hit crops, ecological droughts stress ecosystems, and dust and sand storms can carry billions of tonnes of sand across continents.'],
            ['Warming, rising ocean', 'Warm water expands and melting ice sheets add water, so sea level rises and threatens coastal and island communities. The ocean also absorbs CO<sub>2</sub>, which makes it <b>more acidic</b> and harms corals and marine life.'],
            ['Poverty and displacement', 'Floods can sweep away urban slums; heat makes outdoor jobs hard; people lose homes and livelihoods.'],
            ['Not enough food', 'Crops, fisheries and livestock become less productive; ocean acidification threatens seafood; changes in snow and ice disrupt herding, hunting and fishing in the Arctic.'],
            ['More health risks', 'Diseases spread to new areas, extreme weather raises deaths and overloads health systems, and displacement harms mental health.'],
            ['Loss of species', 'Species are being lost about <b>1,000 times faster</b> than at any other time in recorded history; around <b>one million</b> species are at risk of extinction in the coming decades.']], [1.6, 5.1])
s += F('u3_p12.png', 'Effects of climate change', 13, 6.8)
s += RECALL(['Climate change = long-term shift in temperature and weather; since the 1800s mainly human-driven (fossil fuels).', 'Causes: power, manufacturing, deforestation, transport, food, buildings, over-consumption.', 'Effects: heat, storms, drought, rising and acidifying oceans, poverty, hunger, disease, species loss.', 'Deforestation ≈ 12 million ha/year; transport ≈ ¼ of energy CO<sub>2</sub>; buildings use > ½ of electricity.'])
s += QA('e', 'Define climate change. Is it always caused by humans?', 'Climate change is a long-term shift in temperatures and weather patterns. It can be natural (changes in the Sun\'s activity, large volcanic eruptions), but since the 1800s human activity, mainly burning coal, oil and gas, has been the main driver.')
s += QA('e', 'List any five causes of climate change given in the slides.', [('lines', ['Generating power by burning fossil fuels', 'Manufacturing goods (cement, steel, plastics …)', 'Cutting down forests', 'Using transportation', 'Producing food / powering buildings / consuming too much'])])
s += QA('m', 'Explain how deforestation contributes to climate change in two ways.', [('steps', ['When trees are cut, they release the carbon they had stored, which adds CO<sub>2</sub> to the atmosphere.', 'Fewer trees remain to absorb CO<sub>2</sub> through photosynthesis, so nature\'s ability to keep emissions out of the air is reduced.']), 'About 12 million hectares are lost every year, and deforestation with agriculture and land-use change gives roughly a quarter of global GHG emissions.'])
s += QA('m', 'Why does climate change make storms and floods worse?', [('steps', ['Higher temperature makes more water evaporate, so the air holds more moisture.', 'More moisture means heavier, more extreme rainfall and flooding.', 'Warm ocean surface water feeds cyclones, hurricanes and typhoons, so they become stronger and more destructive.'])])
s += QA('h', 'India\'s grid emission factor is assumed to be 0.8 kg CO<sub>2</sub> per kWh. A building replaces 100 tube lights of 40 W with LED lamps of 18 W. They run 8 hours a day for 300 days a year. Find the energy saved and the CO<sub>2</sub> avoided per year.',
        [('work', '''
Power saved per lamp   = 40 W - 18 W = 22 W
Total power saved      = 22 W x 100 lamps = 2200 W = 2.2 kW
Hours of use per year  = 8 h x 300 days = 2400 h
Energy saved           = 2.2 kW x 2400 h = 5280 kWh
CO2 avoided            = 5280 kWh x 0.8 kg/kWh = 4224 kg
'''), 'Energy saved = <b>5,280 kWh/year</b>; CO<sub>2</sub> avoided = <b>4,224 kg ≈ 4.2 tonnes per year</b>.'])

# ================================================================= 2
s += H1('2. Greenhouse Gases and the Greenhouse Effect')
s += H2('2.1 Greenhouse gases (GHGs)')
s += [P('Greenhouse gases are naturally occurring and human-made gases in the atmosphere that <b>absorb and emit heat</b>, trapping thermal energy. They work like a thermal blanket: sunlight enters the atmosphere, but a large part of the heat that is then re-radiated cannot escape back into space. This is the <b>greenhouse effect</b>, and it keeps the Earth warm enough for life.')]
s += [P('The problem is that burning fossil fuels, deforestation and industrial processes have greatly increased the concentration of these gases, which strengthens the greenhouse effect and causes global warming and climate change.')]
s += TABLE([['Gas', 'Main human sources (extra detail)', 'Relative warming power (GWP, 100 years)*'],
            ['Carbon dioxide (CO<sub>2</sub>)', 'Burning coal, oil and gas; deforestation; cement making', '1 (the reference)'],
            ['Methane (CH<sub>4</sub>)', 'Livestock digestion, rice fields, landfills, coal and gas leaks', '≈ 28'],
            ['Nitrous oxide (N<sub>2</sub>O)', 'Fertilisers and manure, fossil-fuel burning', '≈ 265'],
            ['Water vapour (H<sub>2</sub>O)', 'Evaporation; increases as the air warms (a feedback)', 'not given a GWP'],
            ['CFCs and related gases', 'Old refrigerants, aerosols, foams', 'thousands of times CO<sub>2</sub>']], [1.7, 3.2, 2.0])
s += [P('<i>*Global Warming Potential (GWP) compares how much heat one tonne of a gas traps over 100 years relative to one tonne of CO<sub>2</sub>; the values 28 and 265 are the commonly used IPCC AR5 figures. The slides name the gases; the GWP column is extra detail used in the numericals below.</i>')]
s += H2('2.2 The greenhouse effect step by step')
s += NUM(['Short-wave radiation from the Sun passes through the atmosphere and warms the Earth\'s surface.',
    'The warm surface sends heat back as long-wave (infrared) radiation.',
    'Greenhouse gases absorb a large part of this infrared radiation instead of letting it escape to space.',
    'They re-emit it in all directions, including back down to the surface, so the surface and lower atmosphere stay warm.'])
s += KEY('The <b>natural</b> greenhouse effect is useful: without it the Earth\'s average surface temperature would be far below freezing. The <b>enhanced</b> greenhouse effect, caused by extra human-made GHGs, is what leads to global warming.')
s += F('u3_p14.png', 'The greenhouse effect: GHGs absorb the Sun\'s radiation and do not reflect it back into space', 8.5, 7.5)
s += RECALL(['GHGs absorb and emit heat; main gases: CO<sub>2</sub>, CH<sub>4</sub>, N<sub>2</sub>O and water vapour (plus CFCs).', 'Greenhouse effect = radiation from the Sun absorbed by GHGs and not reflected back to space; it insulates the Earth.', 'Natural effect is useful; enhanced effect causes global warming.'])
s += QA('e', 'Name the major greenhouse gases.', 'Carbon dioxide (CO<sub>2</sub>), methane (CH<sub>4</sub>), nitrous oxide (N<sub>2</sub>O) and water vapour; chlorofluorocarbons (CFCs) are also greenhouse gases.')
s += QA('m', 'Explain the greenhouse effect. Why is it called a "thermal blanket"?', [('steps', ['Sunlight enters the atmosphere and warms the ground.', 'The ground gives out heat (infrared radiation).', 'Greenhouse gases absorb a large share of this heat and send some of it back down.', 'Heat therefore escapes slowly, just as a blanket keeps body heat in, and the Earth stays warm enough for life.'])])
s += QA('m', 'Distinguish between the natural and the enhanced greenhouse effect.', [('lines', ['<b>Natural:</b> caused by gases that are naturally present; it keeps the Earth habitable and prevents it from freezing.', '<b>Enhanced:</b> caused by extra GHGs from burning fossil fuels, deforestation and industry; it traps more heat and leads to global warming.'])])
s += QA('h', 'A farm releases 10 tonnes of methane and 2 tonnes of nitrous oxide in a year. Using GWP(CH<sub>4</sub>) = 28 and GWP(N<sub>2</sub>O) = 265, find the total emission in tonnes of CO<sub>2</sub>-equivalent (CO<sub>2</sub>e).',
        [('work', '''
CO2e from methane        = 10 t x 28  = 280 t CO2e
CO2e from nitrous oxide  =  2 t x 265 = 530 t CO2e
Total                    = 280 + 530  = 810 t CO2e
'''), 'The farm\'s warming effect equals <b>810 tonnes of CO<sub>2</sub></b>, even though it released only 12 tonnes of gas. N<sub>2</sub>O is the larger part (530 of 810).'])

# ================================================================= 3
s += H1('3. Global Warming')
s += [P('<b>Global warming</b> is the long-term warming of the planet\'s overall temperature. The warming trend has existed for a long time, but its pace has increased a lot in the last hundred years because of burning fossil fuels. As the human population grew, so did the amount of coal, oil and natural gas burned.')]
s += [P('When fossil fuels are burned, gases such as carbon dioxide, chlorofluorocarbons, water vapour, methane and nitrous oxide are released. Sunlight passes through the atmosphere, but the heat reflected from the surface cannot escape back into space, so the average global temperature rises.')]
s += BOX('GLOBAL WARMING VS CLIMATE CHANGE', ['<b>Global warming</b> is the rise in the Earth\'s average temperature. <b>Climate change</b> is the wider set of changes that follow: rainfall patterns, storms, sea level, ecosystems and more. Warming is the cause; climate change is the larger result.'])
s += H3('Consequences of global warming (from the slides)')
s += BUL(['Rise in sea levels', 'Melting of glaciers', 'Floods', 'Extreme weather', 'Climate change', 'Threat to life'])
s += H2('3.1 Earth\'s energy budget (figure from the slides)')
s += [P('The figure shows where the Sun\'s energy goes. The numbers are in watts per square metre (W m<super>−2</super>) averaged over the Earth. Incoming solar radiation is 342 W m<super>−2</super>. About 107 W m<super>−2</super> is reflected (77 by clouds, aerosols and the atmosphere, 30 by the surface), and 235 W m<super>−2</super> leaves as outgoing long-wave radiation. The surface radiates 390 W m<super>−2</super> and gets 324 W m<super>−2</super> back as "back radiation" from greenhouse gases; this large return flow is the greenhouse effect.')]
s += F('u3_p15.png', 'Energy flows in the atmosphere (global warming)', 14, 8.5)
s += RECALL(['Global warming = long-term rise of the planet\'s average temperature, speeding up in the last 100 years because of fossil fuels.', 'Results: sea-level rise, melting glaciers, floods, extreme weather, threat to life.', 'Energy balance: incoming 342 = reflected 107 + outgoing 235 (W m<super>−2</super>).'])
s += QA('e', 'What is global warming, and which human activity is mainly responsible for its recent speed-up?', 'Global warming is the long-term warming of the planet\'s overall temperature. Its pace has increased greatly in the last hundred years because of burning fossil fuels (coal, oil and natural gas), whose volume grew with the human population.')
s += QA('m', 'List four consequences of global warming.', 'Rise in sea level, melting of glaciers, floods and other extreme weather, and threat to life (including changes in climate).')
s += QA('h', 'Using the energy-budget figure, check that (a) the Earth is in balance at the top of the atmosphere and (b) the surface is in balance. Incoming solar = 342; reflected = 107; outgoing long-wave = 235. At the surface: absorbed solar = 168, back radiation = 324; surface loses 390 (radiation) + 24 (thermals) + 78 (evaporation/transpiration), all in W m<super>−2</super>.',
        [('work', '''
(a) Top of atmosphere:  IN  = 342
                        OUT = 107 (reflected) + 235 (long-wave) = 342
                        IN = OUT  -> balanced
(b) Surface:            GAINS  = 168 + 324 = 492
                        LOSSES = 390 + 24 + 78 = 492
                        GAINS = LOSSES -> balanced
'''), 'Note that the surface gains almost twice as much energy from back radiation (324) as directly from the Sun (168): that is the effect of greenhouse gases.'])

# ================================================================= 4
s += H1('4. Acid Rain')
s += H2('4.1 What it is and how it forms')
s += [P('<b>Acid rain</b> (acid deposition) means any form of precipitation with acidic components, such as sulphuric or nitric acid, that falls from the atmosphere in wet or dry form. It includes acidic rain, snow, fog, hail and even dust.')]
s += [P('Sulphur dioxide (SO<sub>2</sub>) and nitrogen oxides (NO<sub>x</sub>) react with water and oxygen in the atmosphere to form sulphuric acid (H<sub>2</sub>SO<sub>4</sub>) and nitric acid (HNO<sub>3</sub>). These acids dissolve in water droplets and fall as acid rain, snow or fog.')]
s += [Paragraph(M('SO<sub>2</sub> + oxidants + H<sub>2</sub>O  →  H<sub>2</sub>SO<sub>4</sub> (sulphuric acid)'), S('rx', leftIndent=20, spaceAfter=2)), Paragraph(M('NO<sub>x</sub> + oxidants + H<sub>2</sub>O  →  HNO<sub>3</sub> (nitric acid)'), S('rx2', leftIndent=20, spaceAfter=8))]
s += BOX('pH VALUES', ['Typical pH of acid rain: <b>4.2 – 4.4</b>. Normal rain: about <b>6</b> (the slides use 6). Each pH unit is a factor of 10 in hydrogen-ion concentration, so a small drop in pH means a big rise in acidity.'])
s += [P('<b>Causes:</b> automobiles, combustion in power plants, volcanic eruptions and lightning (SO<sub>2</sub> and NO<sub>x</sub> come from both human and natural sources).')]
s += F('u3_p18.png', 'How SO<sub>2</sub> and NO<sub>x</sub> turn into sulphuric and nitric acid in the atmosphere', 11.5, 6.5)
s += H2('4.2 Effects')
s += BUL(['<b>On water bodies:</b> rivers and lakes become unsuitable for species such as trout and fish; the acidity disrupts their reproduction and fish populations fall.',
          '<b>On buildings and monuments:</b> deterioration and discolouration, especially of limestone and marble, for example the <b>Taj Mahal</b>. (Extra detail: limestone is calcium carbonate, which reacts with sulphuric acid: CaCO<sub>3</sub> + H<sub>2</sub>SO<sub>4</sub> → CaSO<sub>4</sub> + H<sub>2</sub>O + CO<sub>2</sub>.)',
          '<b>On humans:</b> respiratory diseases and skin infections.'])
s += H3('Control measures (extra detail, commonly asked)')
s += BUL(['Use scrubbers (flue-gas desulphurisation) and low-sulphur fuels in power plants and industry.', 'Fit catalytic converters in vehicles to reduce NO<sub>x</sub>.', 'Shift to renewable energy and public transport; use lime to neutralise acidified lakes as a short-term remedy.'])
s += RECALL(['SO<sub>2</sub> + NO<sub>x</sub> + water/oxygen → H<sub>2</sub>SO<sub>4</sub> and HNO<sub>3</sub> → acid rain.', 'pH of acid rain ≈ 4.2–4.4 versus ≈ 6 for normal rain.', 'Effects: dead lakes, damaged limestone/marble monuments (Taj Mahal), respiratory and skin problems.'])
s += QA('e', 'Which two gases mainly cause acid rain and which acids do they form?', 'Sulphur dioxide (SO<sub>2</sub>) forms sulphuric acid (H<sub>2</sub>SO<sub>4</sub>); nitrogen oxides (NO<sub>x</sub>) form nitric acid (HNO<sub>3</sub>).')
s += QA('m', 'Why is the Taj Mahal affected by acid rain?', [('steps', ['The monument is made of marble, a form of calcium carbonate that reacts with acids.', 'Acid rain (and dry acid deposition) eats away the surface and discolours it.', 'Gases from nearby industry and vehicles supply the SO<sub>2</sub> and NO<sub>x</sub> that form the acids.'])])
s += QA('h', 'Normal rain has pH 6 and a sample of acid rain has pH 4.3. How many times higher is the hydrogen-ion concentration in the acid rain? What is the range for pH 4.2 to 4.4?',
        [('work', '''
pH = -log10 [H+]   ->   [H+] = 10^(-pH)
Normal rain  : [H+] = 10^-6
Acid rain    : [H+] = 10^-4.3
Ratio        = 10^-4.3 / 10^-6 = 10^(6 - 4.3) = 10^1.7 = about 50
For pH 4.2   : 10^(6 - 4.2) = 10^1.8 = about 63
For pH 4.4   : 10^(6 - 4.4) = 10^1.6 = about 40
'''), 'The acid rain is about <b>50 times more acidic</b> than normal rain (between 40 and 63 times for pH 4.4 to 4.2).'])

# ================================================================= 5
s += H1('5. Ozone Layer Depletion')
s += H2('5.1 The ozone layer')
s += [P('The ozone layer is the high concentration of ozone (O<sub>3</sub>) found in the <b>stratosphere, 15 to 30 km above the Earth\'s surface</b>. It absorbs <b>97 to 99%</b> of the Sun\'s medium-frequency ultraviolet light (about 200 to 315 nm), which would otherwise damage living things near the surface.')]
s += H2('5.2 How it is depleted')
s += [P('<b>Ozone layer depletion</b> is the gradual thinning of the ozone layer caused by chemicals containing chlorine or bromine released by industry and other human activities. Some compounds release chlorine or bromine when intense UV light in the stratosphere breaks them up. These are called <b>ozone-depleting substances (ODS)</b>. A chlorine or bromine atom meeting an ozone molecule destroys it. Severe depletion creates the <b>"ozone hole"</b> seen over Antarctica in satellite images.')]
s += TABLE([['Releases chlorine', 'Releases bromine'], ['Chlorofluorocarbons (CFCs), hydrochlorofluorocarbons (HCFCs), carbon tetrachloride, methyl chloroform', 'Halons and methyl bromide']], [1, 1])
s += [Paragraph(M('Cl + O<sub>3</sub>  →  ClO + O<sub>2</sub>'), S('o1', leftIndent=20, spaceAfter=1)), Paragraph(M('ClO + O  →  Cl + O<sub>2</sub>'), S('o2', leftIndent=20, spaceAfter=5)), P('<i>Extra detail:</i> the chlorine atom is released again in the second step, so one atom can destroy thousands of ozone molecules, which is why small amounts of ODS cause big damage.')]
s += H2('5.3 Effects of ozone depletion')
s += BUL(['More UV reaches the Earth: non-melanoma skin cancer and cataract (clouding of the eye lens) in humans.', 'Plants: affects growth and development.', 'Marine life: affects motility and survival of phytoplankton, and the early development of fish, shrimp, crab, amphibians and other marine animals.'])
s += KEY('Do not mix up the two problems: the <b>greenhouse effect / global warming</b> is about heat being trapped, while <b>ozone depletion</b> is about less protection from UV radiation. (Extra detail: the 1987 Montreal Protocol is the international treaty that phases out ODS.)')
s += RECALL(['Ozone layer: stratosphere, 15–30 km up; absorbs 97–99% of UV (≈ 200–315 nm).', 'ODS: CFCs, HCFCs, carbon tetrachloride, methyl chloroform (Cl); halons, methyl bromide (Br).', 'Effects: skin cancer, cataract, damage to plants and marine life.'])
s += QA('e', 'Where is the ozone layer and what does it do?', 'It is in the stratosphere, 15 to 30 km above the Earth\'s surface. It absorbs 97–99% of the Sun\'s harmful medium-frequency ultraviolet radiation.')
s += QA('m', 'Name four ozone-depleting substances and say whether they release chlorine or bromine.', [('lines', ['CFCs — chlorine', 'HCFCs — chlorine', 'Halons — bromine', 'Methyl bromide — bromine (carbon tetrachloride and methyl chloroform also release chlorine)'])])
s += QA('h', 'The ozone layer absorbs 97% of incoming UV. Because of depletion this falls to 94%. If 100 units of UV reach the top of the stratosphere, how much reaches the ground before and after? By what factor does the UV exposure change?',
        [('work', '''
Before: transmitted = 100 - 97 = 3 units
After : transmitted = 100 - 94 = 6 units
Factor = 6 / 3 = 2
'''), 'A fall of only 3 percentage points in absorption <b>doubles</b> the UV reaching the surface, which shows why even a small thinning of the layer is serious.'])

# ================================================================= 6
s += H1('6. Carbon Footprint')
s += [P('A <b>carbon footprint</b> is the total amount of greenhouse gases emitted into the atmosphere, mainly carbon dioxide produced by human activities. It measures the impact that an individual, organisation or country has on the environment. Carbon emissions are used to measure it, and the result is usually written in kg or tonnes of CO<sub>2</sub> (or CO<sub>2</sub>e).')]
s += H3('Ways to reduce a carbon footprint')
s += BUL(['Use renewable energy.', 'Reduce energy consumption.', 'Use public transport.', 'Reduce waste generation.'])
s += FORMULA('Carbon footprint = Σ (activity amount × emission factor)<br/>e.g. electricity: kWh × kg CO<sub>2</sub>/kWh; petrol: litres × kg CO<sub>2</sub>/litre; LPG: kg × kg CO<sub>2</sub>/kg.')
s += RECALL(['Carbon footprint = total GHGs (mainly CO<sub>2</sub>) emitted by a person, organisation or country.', 'Reduce it with renewables, lower energy use, public transport and less waste.', 'Footprint = amount of activity × emission factor.'])
s += QA('e', 'What is a carbon footprint? Give two ways to reduce it.', 'It is the total greenhouse gas (mainly CO<sub>2</sub>) emitted because of the activities of a person, organisation or country. It can be reduced by using renewable energy and public transport (also by saving energy and cutting waste).')
s += QA('m', 'Why can one person\'s footprint differ so much from another\'s?', 'Footprint depends on how much energy a person uses at home, how far and how they travel, what they eat, how much they buy and throw away. The slides note that the richest 1% of the world population emit more than the poorest 50%.')
s += QA('h', 'A household uses 250 kWh of electricity per month (assume 0.8 kg CO<sub>2</sub>/kWh), one 14.2 kg LPG cylinder per month (assume 3 kg CO<sub>2</sub> per kg of LPG) and drives 6,000 km a year in a car doing 12 km per litre of petrol (assume 2.3 kg CO<sub>2</sub> per litre). Find the yearly carbon footprint.',
        [('work', '''
Electricity: 250 kWh x 12 months x 0.8 = 2400 kg
LPG        : 14.2 kg x 12 months x 3   = 511.2 kg
Petrol     : 6000 km / 12 km/L = 500 L ; 500 L x 2.3 = 1150 kg
Total      = 2400 + 511.2 + 1150 = 4061.2 kg = about 4.06 tonnes CO2 per year
'''), 'Electricity is the biggest part (2400 kg, about 59%), so switching to renewable power would cut the footprint most.'])

# ================================================================= 7
s += H1('7. Carbon Credit')
s += [P('A <b>carbon credit</b> is a permit that allows the company holding it to emit a certain amount of carbon dioxide or other greenhouse gases. <b>One credit permits the emission of a mass equal to one tonne of CO<sub>2</sub>.</b>')]
s += BUL(['<b>How credits are earned:</b> by an activity that either avoids emitting CO<sub>2</sub> (for example, using renewable energy or saving energy) or absorbs CO<sub>2</sub> that has already been emitted (<b>sequestration</b>, for example planting forests).',
          '<b>Cap and trade:</b> companies receive a fixed number of credits that <b>decline over time</b>. A company that emits less than its allowance can <b>sell its excess credits</b> to another company that needs more.',
          '<b>Authorities:</b> credits are usually issued by a competent authority such as the Bureau of Energy Efficiency (BEE); the Ministry of Power decides the entities, and the limits are set by the Ministry of Environment, Forest and Climate Change (MoEFCC).'])
s += TABLE([['Situation', 'What the company does'], ['Emissions below its allowance', 'Has spare credits → can sell them and earn money'], ['Emissions above its allowance', 'Must buy credits or cut emissions'], ['Allowance falls each year', 'Pressure to invest in clean technology']], [2.5, 3.5])
s += RECALL(['1 carbon credit = permission to emit 1 tonne of CO<sub>2</sub> (or equivalent).', 'Earned by avoiding emissions or absorbing CO<sub>2</sub> (sequestration).', 'Allowances shrink over time; excess credits can be sold.'])
s += QA('e', 'How much CO<sub>2</sub> does one carbon credit allow?', 'One credit allows the emission of one tonne of carbon dioxide (or an equivalent amount of another greenhouse gas).')
s += QA('m', 'Explain how a company can earn carbon credits.', 'By an activity that avoids CO<sub>2</sub> emission (such as switching to renewable energy or saving energy) or that absorbs CO<sub>2</sub> already emitted (sequestration, such as afforestation). The saved or absorbed tonnes are certified as credits that it can keep or sell.')
s += QA('h', 'A factory has an allowance of 50,000 tonnes CO<sub>2</sub> per year and emits 46,500 t. A second factory has the same allowance but emits 52,000 t. Assume a credit price of ₹1,000 per tonne. (a) How many credits can the first factory sell and what is its income? (b) What does it cost the second factory to stay within the law by buying credits?',
        [('work', '''
(a) Spare credits  = 50,000 - 46,500 = 3,500 credits
    Income         = 3,500 x Rs 1,000 = Rs 35,00,000 (Rs 35 lakh)
(b) Shortfall      = 52,000 - 50,000 = 2,000 tonnes
    Cost           = 2,000 x Rs 1,000 = Rs 20,00,000 (Rs 20 lakh)
'''), 'The first factory earns <b>₹35 lakh</b>; the second has to pay <b>₹20 lakh</b> (or reduce its emissions by 2,000 t instead). If the first factory sold 2,000 of its 3,500 credits to the second, both would benefit.'])

# ================================================================= 8
s += H1('8. Sustainable Development Goals (SDGs)')
s += [P('The <b>Sustainable Development Goals (SDGs)</b>, also called the <b>Global Goals</b>, were adopted by the United Nations in <b>2015</b> as a universal call to action to end poverty, protect the planet and ensure that, by <b>2030</b>, all people enjoy peace and prosperity.')]
s += TABLE([['Fact', 'Value'], ['Agenda', '"Transforming our World: the 2030 Agenda for Sustainable Development" (2016–2030)'], ['Number of goals', '17 SDGs'], ['Targets / indicators', '169 targets, measured by 304 indicators'], ['Adopted', '25 September 2015 by 193 countries including India'], ['Implementation began', '1 January 2016'], ['India\'s coordinating body', 'NITI Aayog oversees implementation by ministries and coordinates with the states']], [1.6, 4.4])
s += H2('8.1 From MDGs to SDGs')
s += [P('The SDGs extend the <b>Millennium Development Goals (MDGs)</b>, eight anti-poverty goals that the world committed to achieve by 2015 (all 191 UN members at the time and at least 22 international organisations). The SDGs go further: they address the <b>root causes</b> of poverty and the need for development that works for everyone, and add new areas such as climate change, economic inequality, innovation, sustainable consumption, and peace and justice.')]
s += NUM(['Eradicate extreme poverty and hunger', 'Achieve universal primary education', 'Promote gender equality and empower women', 'Reduce child mortality', 'Improve maternal health', 'Combat HIV/AIDS, malaria and other diseases', 'Ensure environmental sustainability', 'Develop a global partnership for development'])
s += F('u3_p27.png', 'From the 8 MDGs (2000–2015) to the 17 SDGs (2015–2030)', 14, 8.5)
s += H2('8.2 The 17 goals')
s += TABLE([['1 No Poverty', '2 Zero Hunger', '3 Good Health and Well-being'], ['4 Quality Education', '5 Gender Equality', '6 Clean Water and Sanitation'], ['7 Affordable and Clean Energy', '8 Decent Work and Economic Growth', '9 Industry, Innovation and Infrastructure'], ['10 Reduced Inequalities', '11 Sustainable Cities and Communities', '12 Responsible Consumption and Production'], ['13 Climate Action', '14 Life Below Water', '15 Life on Land'], ['16 Peace, Justice and Strong Institutions', '17 Partnerships for the Goals', '']], [1, 1, 1])
s += F('u3_p26.png', 'The 17 Sustainable Development Goals', 12.5, 8)
s += RECALL(['SDGs: UN, 2015; 17 goals, 169 targets, 304 indicators; 193 countries; start 1 Jan 2016; target year 2030.', 'They extend the 8 MDGs (target 2015) and add climate, inequality, innovation, consumption, peace and justice.', 'In India NITI Aayog coordinates with ministries and states.'])
s += QA('e', 'How many SDGs are there and by which year are they to be achieved?', '17 goals, to be achieved by 2030 (as part of the 2030 Agenda, 2016–2030).')
s += QA('m', 'How are the SDGs different from the MDGs?', [('lines', ['MDGs: 8 goals, mainly anti-poverty targets, to be reached by 2015.', 'SDGs: 17 goals that build on MDG successes but also address root causes of poverty and add climate change, inequality, innovation, sustainable consumption, peace and justice.', 'SDGs are universal — they apply to all countries, including India, not only developing ones.'])])
s += QA('h', 'The SDGs have 17 goals and 169 targets. (a) What is the average number of targets per goal? (b) How many more goals are there than in the MDGs? (c) For how many years do the SDGs run (2016 to 2030)?',
        [('work', '''
(a) 169 / 17 = 9.94  -> about 10 targets per goal
(b) 17 - 8   = 9 more goals
(c) 2016 to 2030 inclusive = 2030 - 2016 + 1 = 15 years
'''), 'About <b>10</b> targets per goal, <b>9</b> extra goals, and a <b>15-year</b> implementation period.'])

# ================================================================= 9
s += H1('9. Environmental Legislation in India')
s += H2('9.1 Environmental policy')
s += [P('Environmental policies are either <b>enacted as laws</b> by governing bodies or <b>created and enforced by government agencies</b>. They can come from local, national or foreign governments and cover air and water quality, fossil-fuel extraction, energy conservation, habitat protection and restoration, pesticide use, storage and disposal of hazardous materials, recycling and trafficking in endangered species. Because an environmental policy is interdisciplinary, it draws on technology, economics, and natural and social sciences.')]
s += [P('To make a sustainable policy you need sound knowledge of the real and possible environmental impacts of an activity, and of the technical features, economic cost, social acceptability and side effects of the alternatives. Economic policies usually aim at stimulating production and tend to ignore environmental effects; experience shows they can have more impact on the environment than policies written to protect it.')]
s += H2('9.2 History')
s += BUL(['The detailed framework for environmental protection in India came after the <b>UN Conference on the Human Environment, Stockholm, 1972</b>.', 'This led to the <b>National Council for Environmental Policy and Planning (1972)</b> in the Department of Science and Technology, set up as a regulatory body to oversee environmental concerns.', 'The council was later converted into the <b>Ministry of Environment and Forests</b> (now MoEFCC).'])
s += P('Other legislation and rules listed in the slides cover: <b>Wildlife, Forest Conservation, Biodiversity, the National Green Tribunal and Animal Welfare</b>. (Extra detail for revision: Wildlife (Protection) Act 1972; Forest (Conservation) Act 1980; Biological Diversity Act 2002; National Green Tribunal Act 2010; Prevention of Cruelty to Animals Act 1960.)')
s += H2('9.3 Three major Acts')
s += TABLE([['', 'Water Act, 1974', 'Air Act, 1981', 'Environment (Protection) Act, 1986'],
            ['Full name', 'The Water (Prevention and Control of Pollution) Act', 'The Air (Prevention and Control of Pollution) Act', 'The Environment (Protection) Act'],
            ['Objective', 'Prevention and control of water pollution; maintain or restore wholesomeness and purity of water', 'Prevention, control and abatement of air pollution; set up boards at central and state level', 'Implements the 1972 Stockholm Declaration; protects and improves the environment'],
            ['Bodies', 'CPCB and SPCBs (statutory bodies created under this Act)', 'CPCB and SPCBs given the responsibility', 'Genetic Engineering Appraisal Committee; National Coastal Zone Management Authority (later National Ganga Council)'],
            ['Key powers', 'Set and enforce effluent standards for factories; SPCB controls sewage and industrial discharge by approving, rejecting or granting <b>consent to discharge</b>; CPCB does this for union territories and coordinates SPCBs', 'Limits on particulate matter, lead, CO, SO<sub>2</sub>, NO<sub>x</sub>, VOCs and other toxic substances from vehicles, industry, power plants and engines; state governments can declare <b>air-pollution areas</b>', 'MoEFCC notifies <b>eco-sensitive zones</b> (ecologically fragile areas), e.g. 10 km buffer zones around protected areas']], [0.8, 2, 2, 2.2])
s += RECALL(['Stockholm Conference 1972 → NCEPP 1972 → Ministry of Environment and Forests.', 'Water Act 1974: CPCB/SPCB, effluent standards, consent to discharge.', 'Air Act 1981: control and abatement of air pollution, air-pollution areas.', 'EPA 1986: implements Stockholm Declaration; eco-sensitive zones (10 km buffer).'])
s += QA('e', 'Which international conference led to the development of environmental law in India?', 'The United Nations Conference on the Human Environment held at Stockholm in 1972.')
s += QA('m', 'What are CPCB and SPCB and what powers do they have under the Water Act, 1974?', [('lines', ['CPCB = Central Pollution Control Board; SPCB = State Pollution Control Board. Both are statutory bodies created under the Water Act, 1974.', 'They can set and enforce effluent standards for factories discharging pollutants into water bodies.', 'The SPCB controls sewage and industrial discharge by approving, rejecting or granting consent to discharge; the CPCB does the same for union territories and also frames policy and coordinates the SPCBs.'])])
s += QA('m', 'What is an eco-sensitive zone and under which Act is it notified?', 'Eco-sensitive zones are ecologically fragile areas notified by the MoEFCC under the Environment (Protection) Act, 1986; for example, 10 km buffer zones around protected areas.')
s += QA('h', 'Compare the Water Act 1974, Air Act 1981 and EP Act 1986 on objective and enforcing bodies, and explain why the EP Act is called an "umbrella" Act.',
        [('lines', ['Water Act (1974) — prevent and control water pollution; enforced by CPCB and SPCBs through effluent standards and consent to discharge.', 'Air Act (1981) — prevent, control and abate air pollution; enforced by CPCB and SPCBs; limits on pollutants from industry, vehicles and power plants.', 'EP Act (1986) — wider protection of the environment as a whole, implementing the Stockholm Declaration; it allows notification of eco-sensitive zones and created bodies such as GEAC and the coastal zone authority.']), 'Because it covers the environment as a whole and gives the Central Government powers to act on any environmental matter (including those not covered by the Water and Air Acts), it is described as an umbrella Act.'])

# ================================================================= 10
s += H1('10. Environmental Impact Assessment (EIA)')
s += H2('10.1 Introduction')
s += [P('An <b>environmental assessment</b> is a study to find any unique environmental attributes of a place, from endangered species to existing hazardous waste to historic importance. The procedure makes sure that environmental effects are considered <b>before</b> a final decision is made about a project. It analyses the effects on the environment, reports them, holds a public consultation, and finally makes the decision public after reviewing the comments on the report.')]
s += [P('One of the main strengths of environmental assessment is its <b>flexibility</b>. It can be built into project planning as an essential step, giving attention to social and economic impacts as well as environmental ones, and project managers can use it to make up for gaps in the planning process.')]
s += H3('Time needed for an EA depends on')
s += BUL(['Size and complexity of the proposed project', 'Co-operation received from the sponsor and third parties such as local government', 'Level of interest and support shown by the community', 'Ability of the project team to sustain interest in the EA', 'Skills of the EA team', 'EA techniques used'])
s += F('u3_p40.png', 'Factors that decide the duration of an EA', 11.5, 7)
s += H2('10.2 Benefits')
s += TABLE([['To project sponsors', 'To local communities'], ['Reduced cost and time of project implementation<br/>Cost-saving changes to the project design<br/>Increased project acceptance<br/>Avoided impacts and violations of laws and regulations<br/>Improved project performance<br/>Avoided treatment and clean-up costs', 'A healthier local environment (forests, water sources, farming, recreation, clean urban living)<br/>Improved human health<br/>Maintenance of biodiversity<br/>Decreased resource use<br/>Fewer conflicts over natural resources<br/>Increased community skills, knowledge and pride']], [1, 1])
s += F('u3_p42.png', 'Benefits of environmental assessment', 11.5, 7)
s += H2('10.3 Purposes of EIA')
s += NUM(['<b>To facilitate decision-making.</b> It gives the decision-maker (for example the local authority) a systematic examination of the environmental implications of a proposed action, and sometimes alternatives, before a decision is taken; the decision is supported by the Environmental Impact Statement (EIS).',
          '<b>To aid the formulation of development.</b> Developers often see EIA as a hurdle that is costly and slow. In fact it helps them: it considers location, design and environmental issues in parallel, and shows where a project can be changed to reduce or remove harm. Early consideration leads to environmentally sensitive development, better relations between developer, planning authority and community (a smoother planning permission), and sometimes a financial return.',
          '<b>To be an instrument for sustainable development.</b> Sustainable development means maintaining quality of life, keeping access to natural resources and avoiding lasting environmental damage; global issues like ozone depletion, climate change, deforestation and biodiversity loss need action at several levels, up to global political commitment.'])
s += H2('10.4 Steps in the EIA process')
s += [P('EIA is a <b>systematic process</b> that examines the environmental consequences of development actions <b>in advance</b>. Its emphasis is on <b>prevention</b>, so it is proactive rather than reactive.')]
s += TABLE([['#', 'Step', 'What it does'],
            ['1', 'Project screening', 'Decides whether the project may have significant impacts and so needs an EIA (partly set by EIA regulations of the country)'],
            ['2', 'Scoping', 'Identifies early the key, significant environmental issues out of all possible impacts and alternatives'],
            ['3', 'Consideration of alternatives', 'Checks that other feasible locations, scales, processes, layouts, operating conditions and the <b>no-action option</b> were considered'],
            ['4', 'Description of the project', 'Clarifies purpose, rationale, stages of development, location and processes'],
            ['5', 'Description of the environmental baseline', 'Present and future state of the environment <b>without</b> the project, allowing for natural events and other human activities'],
            ['6', 'Identification of key impacts', 'Brings the previous steps together so all significant adverse and beneficial impacts are identified'],
            ['7', 'Prediction of impacts', 'Estimates the size of change in the environment with the project compared with without it'],
            ['8', 'Evaluation and significance', 'Judges which predicted impacts matter most: Significance = Consequence × Likelihood'],
            ['9', 'Mitigation', 'Measures to avoid, reduce, remedy or compensate significant adverse impacts'],
            ['10', 'Public consultation and participation', 'Improves quality and completeness of the EIA and takes the public\'s views into account'],
            ['11', 'EIS presentation', 'Presents the findings; a vital step — if done badly much good work is lost'],
            ['12', 'Review', 'Systematic appraisal of the quality of the EIS'],
            ['13', 'Decision-making', 'The authority decides to <b>accept, defer or reject</b> the project'],
            ['14', 'Post-decision monitoring', 'Records outcomes of the development after approval; helps project management'],
            ['15', 'Auditing', 'Compares actual outcomes with predicted ones to judge prediction quality and the effectiveness of mitigation; a learning step']], [0.3, 1.9, 4.5])
s += FORMULA('Significance = Consequence × Likelihood')
s += F('u3_p54.png', 'EIA process: a systematic and proactive approach', 15.5, 9.5)
s += F('u3_p55.png', 'Steps in the EIA process (flow chart)', 11, 7)
s += RECALL(['EIA = examine environmental consequences before a decision; proactive, prevention-focused.', 'Purposes: decision-making, aid to development, instrument of sustainable development.', 'Steps: screening → scoping → alternatives → project description → baseline → key impacts → prediction → significance → mitigation → public consultation → EIS → review → decision → monitoring → auditing.', 'Significance = Consequence × Likelihood.'])
s += QA('e', 'What does EIA stand for and when is it carried out?', 'Environmental Impact Assessment. It is carried out before a final decision on a project is taken, to study and report its likely effects on the environment.')
s += QA('e', 'Give two benefits of EIA for project sponsors and two for local communities.', [('lines', ['Sponsors: reduced cost and time of implementation; increased project acceptance (also: avoided legal violations, improved performance).', 'Communities: a healthier local environment and improved human health (also: biodiversity maintained, fewer conflicts over resources).'])])
s += QA('m', 'Explain scoping and the role of the baseline in an EIA.', [('lines', ['<b>Scoping</b> identifies at an early stage the key, significant environmental issues and the alternatives that must be studied, so effort is not wasted on minor issues.', '<b>Baseline</b> describes the present and future state of the environment without the project, so that the impact of the project can be measured as the difference.'])])
s += QA('m', 'Why is post-decision monitoring followed by auditing?', 'Monitoring records the actual outcomes after the project starts; auditing then compares these actual outcomes with the predicted ones. It shows how good the predictions were and how well the mitigation worked, so future EIAs improve.')
s += QA('h', 'Four impacts of a proposed factory are scored on a 1–5 scale for Consequence (C) and Likelihood (L): air emissions (C=4, L=5), noise (C=2, L=4), habitat loss (C=5, L=2), water use (C=3, L=3). Using Significance = C × L, rank them and say which should be mitigated first.',
        [('work', '''
Air emissions : 4 x 5 = 20
Noise         : 2 x 4 =  8
Habitat loss  : 5 x 2 = 10
Water use     : 3 x 3 =  9
Ranking (high to low): Air emissions 20 > Habitat loss 10 > Water use 9 > Noise 8
'''), 'Air emissions score highest (<b>20</b>), so they get priority for mitigation. Note that habitat loss has the highest consequence (5) but is unlikely, so it ranks second.'])
s += QA('h', 'Write a short note on the purposes of EIA and explain how it helps a developer instead of only being a hurdle.', [('steps', ['Purpose 1: helps decision-makers by giving a systematic study of the environmental effects (and alternatives) in the form of an EIS before they decide.', 'Purpose 2: helps developers by showing, early on, where the project can be changed to reduce or remove adverse impacts, saving cost and delay later.', 'Purpose 3: acts as an instrument for sustainable development: keeping quality of life, access to resources and avoiding lasting damage.', 'Early EIA gives smoother planning permission, better relations with the community and sometimes a financial return.'])])

ok = build('/home/sleepy/STUDY:)/sem-1/ess/essclaude/ESS_Unit3_StudyGuide.pdf' if len(sys.argv) < 2 else sys.argv[1], 3, 'Global and National Environmental Issues',
           'This guide covers every topic of the unit exactly as the teacher\'s slides present it, in simple language. Use the tags next to each question to see how hard it is, and try it before reading the answer.', s)
print('BUILD OK' if ok else 'BUILD HAS PROBLEMS')
