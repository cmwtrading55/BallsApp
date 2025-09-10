from fpdf import FPDF

class SAFTPDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'Balls Limited SAFT (Simple Agreement for Future Tokens)', ln=True, align='C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 9)
        self.cell(0, 10, '4BNBalls Ltd, British Virgin Islands', 0, 0, 'C')

    def section_title(self, title):
        self.set_font('Arial', 'B', 13)
        self.cell(0, 10, title, ln=True)
        self.ln(2)

    def section_body(self, body):
        self.set_font('Arial', '', 11)
        self.multi_cell(0, 8, body)
        self.ln(2)

pdf = SAFTPDF()
pdf.add_page()

# Parties
pdf.set_font('Arial', '', 11)
pdf.cell(0, 8, 'This SAFT Agreement (the "Agreement") is made as of [Date] by and between:', ln=True)
pdf.ln(2)
pdf.set_font('Arial', 'B', 11)
pdf.cell(0, 8, 'Company:', ln=True)
pdf.set_font('Arial', '', 11)
pdf.cell(0, 8, 'Balls Ltd (yet to be incorporated), a BVI Limited company registered in British Virgin Islands', ln=True)
pdf.cell(0, 8, 'Company No: TBC', ln=True)
pdf.cell(0, 8, 'Registered Office: TBC', ln=True)
pdf.ln(2)
pdf.set_font('Arial', 'B', 11)
pdf.cell(0, 8, 'Purchaser:', ln=True)
pdf.set_font('Arial', '', 11)
pdf.cell(0, 8, 'Candy', ln=True)
pdf.cell(0, 8, 'Telegram: @TheCryptoCandy', ln=True)
pdf.cell(0, 8, 'Wallet: [To be provided]', ln=True)
pdf.ln(6)

# 1. Introduction
pdf.section_title('1. Introduction')
pdf.section_body('This SAFT Agreement is intended to provide the Purchaser with the right to receive certain tokens of the Company, subject to the terms set forth below.')

# 2. Investment Terms
pdf.section_title('2. Investment Terms')
pdf.section_body('Purchase Amount: $200,000 USD\nToken Offer Price: $0.0075 per token')

# 3. Conversion Trigger
pdf.section_title('3. Conversion Trigger')
pdf.section_body('The SAFT will convert into tokens upon the occurrence of one or more of the following events:\n- Initial Coin Offering (ICO)\n- Acquisition')

# 4. Conversion Mechanics
pdf.section_title('4. Conversion Mechanics')
pdf.section_body('- Token Distribution: Upon the ICO, the Purchase Amount will convert into tokens at the token offer price as set out in Appendix 1.\n- Liquidity Event: In the event of an acquisition, the SAFT will convert into tokens or equivalent value.\n- Dissolution Event: If the Company dissolves before conversion, the Purchaser will be entitled to receive the Purchase Amount back, subject to available funds.')

# 5. Investor Rights
pdf.section_title('5. Investor Rights')
pdf.section_body('- Participation Rights: The Purchaser will have the right to participate in future token offerings on a pro-rata basis.')

# 6. Company Representations and Warranties
pdf.section_title('6. Company Representations and Warranties')
pdf.section_body('- Authority: The Company represents that it has the authority to enter into this Agreement.\n- Compliance: The Company assures that it is in compliance with all applicable laws and regulations.')

# 7. Miscellaneous Provisions
pdf.section_title('7. Miscellaneous Provisions')
pdf.section_body('- Governing Law: This Agreement will be governed by and construed in accordance with the laws of England and Wales.')

pdf.ln(8)
pdf.set_font('Arial', '', 11)
pdf.cell(0, 8, 'Company Representative:', ln=True)
pdf.cell(0, 8, 'Nicholas Collinson', ln=True)
pdf.cell(0, 8, 'Director', ln=True)

# Appendix 1
pdf.add_page()
pdf.set_font('Arial', 'B', 13)
pdf.cell(0, 10, 'Appendix 1 - Vesting Schedule and Token Allocation (Candy Deal Terms)', ln=True)
pdf.ln(2)

pdf.set_font('Arial', 'B', 11)
pdf.cell(0, 8, '1. Token Details', ln=True)
pdf.set_font('Arial', '', 11)
pdf.multi_cell(0, 8, 'Token Name: BallsApp ($BALLS)\nToken Type: Utility Token (ERC-20 or equivalent standard on supported chains)\nTotal Supply: 4,000,000,000 $BALLS\nPurchaser Allocation: 26,666,666 $BALLS\nPurchase Price: $0.0075 USD per token\nTotal Consideration: $200,000 USD')
pdf.ln(2)

pdf.set_font('Arial', 'B', 11)
pdf.cell(0, 8, '2. Vesting Schedule (Bespoke Terms)', ln=True)
pdf.set_font('Arial', '', 11)
pdf.multi_cell(0, 8, 'Subject to the terms and conditions of the SAFT, the Purchaser\'s tokens shall be delivered according to the following revised vesting schedule:\nTGE Unlock (Token Generation Event): 20% of allocated tokens (5,333,333 $BALLS) shall be released on the date of mint and official launch (anticipated to be July 31, 2025).\nMonthly Vesting: The remaining 80% (21,333,333 $BALLS) shall vest in equal monthly installments over a period of 6 months following the TGE.\nMonthly Vesting Amount: 3,555,555.50 $BALLS (rounded to the nearest whole token)\nFinal Vesting Date: January 31, 2026')
pdf.ln(2)

pdf.set_font('Arial', 'B', 11)
pdf.cell(0, 8, '3. Cliff and Lock-Up', ln=True)
pdf.set_font('Arial', '', 11)
pdf.multi_cell(0, 8, 'There is no cliff period beyond the TGE.\nVesting begins immediately after the TGE, with monthly releases on the final calendar day of each month.')
pdf.ln(2)

pdf.set_font('Arial', 'B', 11)
pdf.cell(0, 8, '4. Transferability', ln=True)
pdf.set_font('Arial', '', 11)
pdf.multi_cell(0, 8, 'All token transfers remain subject to the applicable regulatory and contractual restrictions, including compliance with securities law and Know Your Customer (KYC) / Anti-Money Laundering (AML) requirements.')
pdf.ln(2)

pdf.set_font('Arial', 'B', 11)
pdf.cell(0, 8, '5. Additional Notes', ln=True)
pdf.set_font('Arial', '', 11)
pdf.multi_cell(0, 8, 'This bespoke vesting schedule is provided in recognition of the Purchaser\'s strategic role and material early support for the project.\nToken delivery is conditional upon the successful minting and deployment of the $BALLS token and the availability of a compliant distribution mechanism.')

pdf.output('BallsApp_SAFT_Agreement.pdf') 