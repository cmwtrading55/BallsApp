from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'BallsApp ($BALLS) KOL Executive Playbook', ln=True, align='C')
        self.ln(5)

    def section_title(self, title):
        self.set_font('Arial', 'B', 13)
        self.cell(0, 10, title, ln=True)
        self.ln(2)

    def section_body(self, body):
        self.set_font('Arial', '', 11)
        self.multi_cell(0, 8, body)
        self.ln(2)

pdf = PDF()
pdf.add_page()

# Overview
pdf.section_title('Why $BALLS Will Dominate')
pdf.section_body(
    'BallsApp is not just another token launch--this is a movement. $BALLS is engineered for explosive growth, with a total supply of 4,000,000,000 tokens and a pre-sale designed to reward early believers. With a hyper-engaged community, major exchange listings, and a KOL-first approach, $BALLS is set to become the most talked-about launch of the year.'
)
pdf.ln(6)

# Tokenomics Snapshot
pdf.section_title('Tokenomics: Built for Moon Mission')
pdf.section_body(
    'Total Supply: 4,000,000,000 $BALLS\n'
    'Pre-sale Allocation: 400,000,000 $BALLS (10% of total supply)\n'
    'Pre-sale Start: July 5th\n'
    'Minimum Launch Price: $0.05\n'
    'Tokenomics are designed for maximum upside and long-term sustainability.'
)
pdf.ln(6)

# Pre-sale Tranches Table
pdf.section_title('Pre-sale Tranches: Early Entry, Max Gains')
pdf.set_font('Arial', 'B', 10)
pdf.cell(50, 8, 'Tranche', 1)
pdf.cell(30, 8, 'Tokens Sold', 1)
pdf.cell(35, 8, 'Price/Token (USD)', 1)
pdf.cell(35, 8, '% of Supply', 1)
pdf.ln()
pdf.set_font('Arial', '', 10)
tranches = [
    ('Proof-of-concept', '33,333,333', '$0.00750', '0.83%'),
    ('Early Access', '64,884,903', '$0.01165', '1.61%'),
    ('Private Sale', '82,908,314', '$0.01809', '2.07%'),
    ('Public Pre-sale A', '133,451,093', '$0.02810', '3.34%'),
    ('Public Pre-sale B', '85,922,357', '$0.04364', '2.15%'),
    ('Total', '400,000,000', '-', '10%'),
]
for t in tranches:
    pdf.cell(50, 8, t[0], 1)
    pdf.cell(30, 8, t[1], 1)
    pdf.cell(35, 8, t[2], 1)
    pdf.cell(35, 8, t[3], 1)
    pdf.ln()
pdf.ln(10)

# Add a page break so Token Allocation starts on page 2
pdf.add_page()

# Token Allocation
pdf.section_title('Token Allocation: Powering the Ecosystem')
pdf.section_body(
    'Ecosystem Growth: 20%\n'
    'Marketing & Rewards: 20%\n'
    'Team: 15%\n'
    'Partners & Technology: 15%\n'
    'Liquidity & Support: 15%\n'
    'Private Sale: 10%\n'
    'Reserve / Treasury: 2.5%\n'
    'Public Sale: 2.5%'
)
pdf.ln(8)

# Key Milestones
pdf.section_title('Key Milestones: The Road to Viral')
pdf.section_body(
    'July 5th: Pre-sale goes live--get in before the crowd.\n'
    'July 24th: CoinDCX blasts BallsApp to their full client base.\n'
    'July 31st: $BALLS mints and launches on CoinDCX, MEXC, and Gate.io. The rocket ignites.'
)
pdf.ln(8)

# Monthly Prize Draws & Liquidity
pdf.section_title('Monthly Prize Draws: Massive Liquidity, Massive Hype')
pdf.section_body(
    "Starting July, BallsApp will run multiple monthly prize draws with unique, high-value prizes promoted by our top-tier Influencers and KOLs. Here's the alpha: 30% of every ticket draw is used to buy $BALLS and inject it straight into liquidity pools. This means relentless buy pressure, deep liquidity, and a price floor that rewards early holders as tokens unlock during vesting. No other project is fueling their ecosystem like this."
)
pdf.ln(10)

# Add a page break so Pre-sale Mechanics starts on page 3
pdf.add_page()

# Pre-sale Purchase Mechanics
pdf.section_title('Pre-sale Mechanics: Designed for Diamond Hands')
pdf.section_body(
    'Vesting:\n'
    '- 10% of your tokens airdropped at mint (July 31st)\n'
    '- 8.18% airdropped monthly for the next 11 months\n'
    '- Total vesting period: 11 months\n'
    'This structure ensures a strong, committed community and a healthy chart.'
)
pdf.ln(8)

# KOL Benefits
pdf.section_title('KOL Benefits: Your Influence, Your Bag')
pdf.section_body(
    '- Daily Payment: Get paid in stablecoin every day, as a % of funds received via your unique referral URL.\n'
    '- Custom URL: Track your impact and earnings in real time.\n'
    '- Marketing Arsenal: Access exclusive content, including celebrity videos (Ravi Shastri and more).\n'
    '- Early Access: Be the first to ride the wave with major exchange listings and viral campaigns.\n'
    '- Community Power: Join a movement built for KOLs, by KOLs.'
)
pdf.ln(8)

# Why BallsApp
pdf.section_title('Why BallsApp? The Ultimate KOL Launchpad')
pdf.section_body(
    '- Hyper-Bullish Tokenomics: Transparent, aggressive, and built for upside.\n'
    '- Major Exchange Listings: CoinDCX, MEXC, Gate.io--maximum exposure from day one.\n'
    '- Relentless Buy Pressure: 30% of every prize draw ticket goes to buying $BALLS for liquidity.\n'
    '- KOL-First: Transparent, daily compensation and a platform designed for your success.'
)
pdf.ln(10)

pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, 'Ready to lead the next crypto wave? Contact the BallsApp team for your unique referral link.', ln=True)
pdf.ln(8)
pdf.set_font('Arial', '', 11)
pdf.cell(0, 10, 'Pre-sale starts July 5th. Secure your spot. Secure your bag. Let\'s make history.', ln=True)
pdf.ln(8)

pdf.output('BallsApp_KOL_Executive_Summary.pdf') 