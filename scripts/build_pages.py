"""Build the static pages using shared layouts; no third-party dependencies."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def read(path):
    return (ROOT / path).read_text()

def render(template, values):
    for key, value in values.items():
        template = template.replace('{{' + key + '}}', value)
    return template

def tape(kind='top'):
    return f'<span class="scrapbook-tape tape-{kind}" aria-hidden="true"><img src="/assets/tape.png" alt=""></span>'

team_cards = ''.join(f'<div class="team-polaroid" role="img" aria-label="Team member photo placeholder {i + 1}"><img class="team-frame" src="/assets/polaroid.png" alt=""><img class="team-pin" src="/assets/pin.png" alt=""></div>' for i in range(8))
event_rows = []
for tags, signup in [(['Networking'], True), (['Social', 'Food Provided'], True), (['Networking'], True), (['Networking', 'Food Provided'], False), (['Networking'], True), (['Social', 'Food Provided'], True), (['Social'], False)]:
    signup_text = '<button class="event-signup" data-missing-link="Event sign-up">https://bit.ly/something</button>' if signup else 'N/A'
    tag_html = ''.join(f'<span class="event-tag tag-{tag.split()[0].lower()}">{tag}</span>' for tag in tags)
    event_rows.append(f'<tr><td data-label="Time"><time datetime="2026-10-27">Oct 27, 2026</time><br>6pm - 8 pm</td><td data-label="Venue">E5 Second Floor<br>Event Space</td><td data-label="Event">Panel Discussion:<br>Hydro One</td><td data-label="Event Info"><p>Sign-up link: {signup_text}</p><div class="event-tags">{tag_html}</div></td></tr>')

stats = ''.join(f'<div>{tape()}<dt>{label}</dt><dd>xx</dd></div>' for label in ['sponsors this year', 'events supported', 'students reached', 'supporting since'])
logos = [('hydro-one.png','Hydro One','https://www.hydroone.com/'),('capital-one.png','Capital One','https://www.capitalone.ca/'),('siemens.png','Siemens','https://www.siemens.com/'),('point-click-care.png','PointClickCare','https://pointclickcare.com/')]
sponsor_cards = []
for i in range(9):
    decoration = tape(['top', 'middle', 'bottom'][i // 3])
    if i < len(logos):
        src, name, href = logos[i]
        sponsor_cards.append(f'<a class="sponsor-card logo-{i}" href="{href}" target="_blank" rel="noopener noreferrer" aria-label="Visit {name} website (opens in a new tab)">{decoration}<img class="sponsor-logo" src="/assets/{src}" alt="{name}"></a>')
    else:
        sponsor_cards.append(f'<div class="sponsor-card" role="img" aria-label="Sponsor logo placeholder">{decoration}</div>')
benefits = [('Meet future talent', 'Connect with engineering students early, at events built around skills and community.'),('Visibility on campus', 'Your logo on our website, posters and social media, in front of the Waterloo engineering community.'),('Support Inclusion', 'Help make engineering more welcoming and accessible for women and everyone who joins us.')]
benefit_cards = ''.join(f'<article class="benefit-card"><div class="benefit-photo"><img src="/assets/polaroid.png" alt=""><h3>{title}</h3></div><p>{copy}</p></article>' for title, copy in benefits)
package_cards=[]
for title, count in [('Supporter',7),('Partner',8),('Champion',7)]:
    popular = title == 'Partner'
    package_cards.append('<article class="package-card'+(' popular' if popular else '')+'">'+tape('package')+f'<h3 class="handwritten">{title}</h3><p class="package-price">$xxx.xx</p><ul>'+('<li>Placeholder</li>' * count)+'</ul>'+('<p class="popular-label handwritten">MOST POPULAR!</p>' if popular else '')+'</article>')
steps=[('Say hello','Fill in the form below or email us at wie@uwaterloo.ca.'),('Chat with us',"We'll set up a quick call to talk goals and what you'd like to support."),('Pick a package','Choose a package, or let us build a custom one with you.'),('Build together',"Send your logo, and we'll get you on the page and at our events.")]
step_html=''.join(f'<li><span class="step-number handwritten">{i+1}</span><img class="step-gear" src="/assets/pink-gear.png" alt=""><h3>{title}</h3><p>{copy}</p></li>' for i,(title,copy) in enumerate(steps))
expansions={'team-cards':team_cards,'event-rows':''.join(event_rows),'sponsor-stats':stats,'sponsor-cards':''.join(sponsor_cards),'benefit-cards':benefit_cards,'package-cards':''.join(package_cards),'sponsor-steps':step_html}
pages=[('home','Home','Women In<br>Engineering','index.html',''),('about','About Us','About Us','about-us/index.html','interior-hero'),('events','Events','Events','events/index.html','interior-hero'),('sponsors','Our Sponsors','Our Sponsors','our-sponsors/index.html','interior-hero sponsor-hero')]
for slug,title,hero_title,destination,hero_class in pages:
    header=read('templates/header.html')
    active='/' if slug=='home' else '/'+destination.removesuffix('index.html')
    header=header.replace(f'href="{active}">{title}',f'href="{active}" aria-current="page">{title}')
    page=render(read('templates/base.html'), {'title':title,'description':f'{title} — Women in Engineering at the University of Waterloo.','page-class':f'page-{slug}','header':header,'hero':render(read('templates/hero.html'),{'hero-title':hero_title,'hero-class':hero_class}),'content':render(read(f'pages/{slug}.html'),expansions),'footer':read('templates/footer.html'),'notice':read('templates/notice.html')})
    assert '{{' not in page, destination
    path=ROOT/destination
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(page)
print('Built Home, About Us, Events, and Our Sponsors.')
