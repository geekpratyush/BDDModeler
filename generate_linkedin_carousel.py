import os
from PIL import Image, ImageDraw, ImageFont

# Canvas Configuration
WIDTH, HEIGHT = 1080, 1080
BG_DARK = (11, 15, 25)         # #0b0f19
CARD_BG = (21, 28, 44)         # #151c2c
ACCENT_BLUE = (59, 130, 246)   # #3b82f6
TEXT_WHITE = (241, 245, 249)   # #f1f5f9
TEXT_MUTED = (148, 163, 184)   # #94a3b8
BORDER_COLOR = (31, 41, 55)    # #1f2937
GREEN_SUCCESS = (16, 185, 129) # #10b981
PURPLE_TAG = (139, 92, 246)    # #8b5cf6

FONT_PATH_BOLD = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
FONT_PATH_REG = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'

font_title = ImageFont.truetype(FONT_PATH_BOLD, 42)
font_subtitle = ImageFont.truetype(FONT_PATH_BOLD, 26)
font_body = ImageFont.truetype(FONT_PATH_REG, 22)
font_bold = ImageFont.truetype(FONT_PATH_BOLD, 22)
font_pill = ImageFont.truetype(FONT_PATH_BOLD, 18)
font_footer = ImageFont.truetype(FONT_PATH_BOLD, 18)

def draw_header_footer(draw, slide_num, total_slides, category="ROUTEFORGE BDD STUDIO"):
    # Background
    draw.rectangle([(0, 0), (WIDTH, HEIGHT)], fill=BG_DARK)
    
    # Outer Card Frame
    draw.rectangle([(20, 20), (WIDTH - 20, HEIGHT - 20)], outline=BORDER_COLOR, width=2)
    
    # Top Category Pill
    pill_text = f" {category} "
    draw.rectangle([(50, 45), (420, 85)], fill=CARD_BG, outline=ACCENT_BLUE, width=1)
    draw.text((65, 53), category, fill=ACCENT_BLUE, font=font_pill)
    
    # Slide Indicator
    ind_text = f"Slide {slide_num} of {total_slides}"
    draw.text((WIDTH - 180, 53), ind_text, fill=TEXT_MUTED, font=font_pill)
    
    # Footer Banner
    draw.line([(40, HEIGHT - 80), (WIDTH - 40, HEIGHT - 80)], fill=BORDER_COLOR, width=1)
    footer_left = "Architected by Pratyush Ranjan Mishra"
    footer_right = "https://geekpratyush.github.io/BDDModeler/"
    draw.text((50, HEIGHT - 60), footer_left, fill=TEXT_WHITE, font=font_footer)
    draw.text((WIDTH - 440, HEIGHT - 60), footer_right, fill=ACCENT_BLUE, font=font_footer)

def create_slide_1():
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_DARK)
    draw = ImageDraw.Draw(img)
    draw_header_footer(draw, 1, 7, "ENTERPRISE BDD REQUIREMENT STUDIO")
    
    # Hero Title
    draw.text((50, 140), "RouteForge BDD Studio", fill=TEXT_WHITE, font=ImageFont.truetype(FONT_PATH_BOLD, 52))
    draw.text((50, 210), "v1.0 Enterprise", fill=ACCENT_BLUE, font=ImageFont.truetype(FONT_PATH_BOLD, 46))
    
    # Subtitle
    draw.text((50, 290), "Data-Agnostic Behavioral Requirement Engineering", fill=TEXT_MUTED, font=font_subtitle)
    draw.text((50, 330), "For Business Analysts, Architects, & QA Engineers", fill=TEXT_MUTED, font=font_subtitle)
    
    # Feature Badges
    badges = ["ISO 20022 XML", "SWIFT MT103", "ACH FlatFile", "JSON", "YAML", "Jira Export"]
    bx, by = 50, 400
    for b in badges:
        bw = len(b) * 14 + 24
        draw.rectangle([(bx, by), (bx + bw, by + 40)], fill=CARD_BG, outline=BORDER_COLOR, width=1)
        draw.text((bx + 12, by + 8), b, fill=GREEN_SUCCESS, font=font_pill)
        bx += bw + 15
        if bx > WIDTH - 200:
            bx = 50
            by += 55

    # Main Center Box
    draw.rectangle([(50, 520), (WIDTH - 50, 930)], fill=CARD_BG, outline=BORDER_COLOR, width=2)
    draw.text((80, 550), "🌟 Why Enterprise BAs Love RouteForge:", fill=TEXT_WHITE, font=font_subtitle)
    
    bullets = [
        "1. Complete Data Freedom: XML, SWIFT, FlatFiles, JSON directly in Gherkin.",
        "2. 1-Click Permutation Simulation: Real-time <placeholder> variable substitution.",
        "3. Automatic Jira Story & Sub-Task Generator (Wiki, Markdown, JSON).",
        "4. Local Directory Sync: Scan local .feature folders & subfolder trees.",
        "5. Zero Dependencies: Runs pure client-side with 100% data privacy."
    ]
    
    y = 610
    for bullet in bullets:
        draw.text((80, y), bullet, fill=TEXT_WHITE, font=font_body)
        y += 60
        
    return img

def create_slide_2():
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_DARK)
    draw = ImageDraw.Draw(img)
    draw_header_footer(draw, 2, 7, "THE BA CHALLENGE")
    
    draw.text((50, 130), "Why Conventional BDD Tools Fail", fill=TEXT_WHITE, font=font_title)
    draw.text((50, 190), "In Banking & Enterprise FinTech Systems", fill=ACCENT_BLUE, font=font_subtitle)
    
    # Problem Box
    draw.rectangle([(50, 260), (WIDTH - 50, 560)], fill=CARD_BG, outline=(239, 68, 68), width=2)
    draw.text((80, 290), "❌ The Pain Points of Legacy BDD Tools:", fill=(239, 68, 68), font=font_subtitle)
    
    pains = [
        "• Rigid JSON Lock-in: Enterprise banking runs on ISO 20022 XML & SWIFT MT.",
        "• Hard to Model FlatFiles: NACHA ACH & ISO 8583 settlement flat lines fail.",
        "• Manual Jira Copy-Paste: BAs waste hours converting Gherkin to Jira Stories.",
        "• Clunky Mocking: Hard to verify payload variable substitution dynamically."
    ]
    y = 350
    for p in pains:
        draw.text((80, y), p, fill=TEXT_WHITE, font=font_body)
        y += 48

    # Solution Box
    draw.rectangle([(50, 600), (WIDTH - 50, 930)], fill=CARD_BG, outline=GREEN_SUCCESS, width=2)
    draw.text((80, 630), "✅ The RouteForge BDD Studio Solution:", fill=GREEN_SUCCESS, font=font_subtitle)
    
    sols = [
        "• Format-Agnostic DocStrings (\"\"\"xml, \"\"\"swift, \"\"\"flatfile, \"\"\"json).",
        "• 1-Click Sample Presets: ISO 20022 pacs.008 XML & SWIFT MT103 templates.",
        "• Automated Jira Generator: 1-click Wiki Markup & Sub-Task export.",
        "• Dynamic Interactive Simulator: 1-click data table substitution."
    ]
    y = 690
    for s in sols:
        draw.text((80, y), s, fill=TEXT_WHITE, font=font_body)
        y += 50

    return img

def create_slide_3():
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_DARK)
    draw = ImageDraw.Draw(img)
    draw_header_footer(draw, 3, 7, "MULTI-FORMAT PAYLOAD ENGINE")
    
    draw.text((50, 130), "Multi-Format Data Payload Editor", fill=TEXT_WHITE, font=font_title)
    draw.text((50, 190), "ISO 20022 XML • SWIFT MT103 • ACH FlatFiles • JSON • YAML", fill=ACCENT_BLUE, font=font_pill)
    
    # Embed Screenshot
    shot_path = "/home/pratyush/software/BDDModeler/assets/editor_showcase.png"
    if os.path.exists(shot_path):
        shot = Image.open(shot_path)
        shot = shot.resize((980, 540))
        img.paste(shot, (50, 250))
        draw.rectangle([(50, 250), (1030, 790)], outline=BORDER_COLOR, width=2)
        
    # Feature Bullet Box
    draw.rectangle([(50, 810), (WIDTH - 50, 930)], fill=CARD_BG, outline=ACCENT_BLUE, width=1)
    draw.text((70, 830), "⚡ Key Capability:", fill=ACCENT_BLUE, font=font_bold)
    draw.text((70, 865), "Business Analysts specify real XML tags, SWIFT blocks, or ACH lines directly inside", fill=TEXT_WHITE, font=font_body)
    draw.text((70, 895), "Gherkin step containers with 1-click sample template insertion.", fill=TEXT_MUTED, font=font_body)
    
    return img

def create_slide_4():
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_DARK)
    draw = ImageDraw.Draw(img)
    draw_header_footer(draw, 4, 7, "INTERACTIVE SIMULATION")
    
    draw.text((50, 130), "1-Click Permutation Simulation", fill=TEXT_WHITE, font=font_title)
    draw.text((50, 190), "Real-Time <placeholder> Variable Substitution & Pass/Fail Status", fill=ACCENT_BLUE, font=font_pill)
    
    # Embed Screenshot
    shot_path = "/home/pratyush/software/BDDModeler/assets/simulation_showcase.png"
    if os.path.exists(shot_path):
        shot = Image.open(shot_path)
        shot = shot.resize((980, 540))
        img.paste(shot, (50, 250))
        draw.rectangle([(50, 250), (1030, 790)], outline=BORDER_COLOR, width=2)

    # Feature Bullet Box
    draw.rectangle([(50, 810), (WIDTH - 50, 930)], fill=CARD_BG, outline=GREEN_SUCCESS, width=1)
    draw.text((70, 830), "⚡ Step-by-Step Test Engine:", fill=GREEN_SUCCESS, font=font_bold)
    draw.text((70, 865), "Executes Gherkin scenario steps in sequence. Replaces <placeholder> variables in XML", fill=TEXT_WHITE, font=font_body)
    draw.text((70, 895), "and JSON payloads with data table row values in real time.", fill=TEXT_MUTED, font=font_body)

    return img

def create_slide_5():
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_DARK)
    draw = ImageDraw.Draw(img)
    draw_header_footer(draw, 5, 7, "JIRA STORY & TASK GENERATOR")
    
    draw.text((50, 130), "Jira User Story & Sub-Task Generator", fill=TEXT_WHITE, font=font_title)
    draw.text((50, 190), "1-Click Agile Ticket Creation (Wiki Markup • Markdown • REST JSON)", fill=ACCENT_BLUE, font=font_pill)
    
    # Embed Screenshot
    shot_path = "/home/pratyush/software/BDDModeler/assets/jira_showcase.png"
    if os.path.exists(shot_path):
        shot = Image.open(shot_path)
        shot = shot.resize((980, 540))
        img.paste(shot, (50, 250))
        draw.rectangle([(50, 250), (1030, 790)], outline=BORDER_COLOR, width=2)

    # Feature Bullet Box
    draw.rectangle([(50, 810), (WIDTH - 50, 930)], fill=CARD_BG, outline=PURPLE_TAG, width=1)
    draw.text((70, 830), "⚡ Zero Manual Copy-Pasting:", fill=PURPLE_TAG, font=font_bold)
    draw.text((70, 865), "Automatically converts BDD scenarios into Jira Acceptance Criteria with code blocks", fill=TEXT_WHITE, font=font_body)
    draw.text((70, 895), "and auto-generated Sub-Tasks. 1-click Copy to Clipboard & Download.", fill=TEXT_MUTED, font=font_body)

    return img

def create_slide_6():
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_DARK)
    draw = ImageDraw.Draw(img)
    draw_header_footer(draw, 6, 7, "PROJECT & DOMAIN MANAGEMENT")
    
    draw.text((50, 130), "Folder Groups & Custom Domains", fill=TEXT_WHITE, font=font_title)
    draw.text((50, 190), "Organize Complex Project Subfolders & Industry Templates", fill=ACCENT_BLUE, font=font_subtitle)
    
    # Group Cards Layout
    draw.rectangle([(50, 260), (510, 570)], fill=CARD_BG, outline=BORDER_COLOR, width=2)
    draw.text((80, 290), "📁 Subfolder Group Management", fill=TEXT_WHITE, font=font_subtitle)
    draw.text((80, 340), "• Native File System directory scan", fill=TEXT_MUTED, font=font_body)
    draw.text((80, 385), "• Recursive mapping of local .feature folders", fill=TEXT_MUTED, font=font_body)
    draw.text((80, 430), "• Dedicated '+ Group' button in sidebar", fill=TEXT_MUTED, font=font_body)
    draw.text((80, 475), "• Safe '✕ Group' folder deletion", fill=TEXT_MUTED, font=font_body)
    draw.text((80, 520), "• Workspace Tabs Bar for open files", fill=TEXT_MUTED, font=font_body)

    draw.rectangle([(570, 260), (1030, 570)], fill=CARD_BG, outline=BORDER_COLOR, width=2)
    draw.text((600, 290), "🌐 Custom Domain Engine", fill=TEXT_WHITE, font=font_subtitle)
    draw.text((600, 340), "• Built-in Domains: Banking, Retail, Health", fill=TEXT_MUTED, font=font_body)
    draw.text((600, 385), "• '+ New Domain' custom industry creator", fill=TEXT_MUTED, font=font_body)
    draw.text((600, 430), "• E.g. Insurance, Freight, Telecom", fill=TEXT_MUTED, font=font_body)
    draw.text((600, 475), "• Persistent localStorage storage", fill=TEXT_MUTED, font=font_body)
    draw.text((600, 520), "• Instant domain workspace switching", fill=TEXT_MUTED, font=font_body)

    # Bottom Summary Card
    draw.rectangle([(50, 610), (WIDTH - 50, 930)], fill=CARD_BG, outline=ACCENT_BLUE, width=2)
    draw.text((80, 640), "🏛️ Pre-Built Banking Templates Included:", fill=ACCENT_BLUE, font=font_subtitle)
    
    b_bullets = [
        "1. Intraday Clearing Line Utilization & Limit Queueing",
        "2. Excess Approval & Hierarchy Dual Signoff Escalation",
        "3. Daily Overdraft & Limit/Sublimit Earmarking Releases",
        "4. ISO 20022 MX pacs.008 XML to SWIFT MT103 Message Transformation",
        "5. Sanctions Screening & OFAC Quarantine Engine"
    ]
    y = 700
    for b in b_bullets:
        draw.text((80, y), b, fill=TEXT_WHITE, font=font_body)
        y += 42

    return img

def create_slide_7():
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_DARK)
    draw = ImageDraw.Draw(img)
    draw_header_footer(draw, 7, 7, "TRY IT LIVE TODAY")
    
    draw.text((50, 130), "Try RouteForge BDD Studio Live!", fill=TEXT_WHITE, font=font_title)
    draw.text((50, 190), "100% Free & Open-Source Zero-Dependency Tool", fill=GREEN_SUCCESS, font=font_subtitle)
    
    # CTA Big Box
    draw.rectangle([(50, 260), (WIDTH - 50, 550)], fill=CARD_BG, outline=ACCENT_BLUE, width=2)
    draw.text((80, 290), "🚀 Experience the Live Application:", fill=TEXT_WHITE, font=font_title)
    draw.text((80, 370), "👉 https://geekpratyush.github.io/BDDModeler/", fill=ACCENT_BLUE, font=ImageFont.truetype(FONT_PATH_BOLD, 30))
    draw.text((80, 430), "🐙 GitHub: https://github.com/geekpratyush/BDDModeler", fill=TEXT_WHITE, font=font_subtitle)
    draw.text((80, 480), "🔗 LinkedIn: https://www.linkedin.com/in/leadtherightway/", fill=TEXT_WHITE, font=font_subtitle)

    # Author Bio Card
    draw.rectangle([(50, 590), (WIDTH - 50, 930)], fill=CARD_BG, outline=BORDER_COLOR, width=2)
    draw.text((80, 620), "👨‍💻 About the Author & Architect:", fill=TEXT_WHITE, font=font_subtitle)
    draw.text((80, 670), "Pratyush Ranjan Mishra", fill=ACCENT_BLUE, font=ImageFont.truetype(FONT_PATH_BOLD, 28))
    draw.text((80, 715), "Enterprise Systems Architect & Requirement Engineering Specialist", fill=TEXT_MUTED, font=font_body)
    draw.text((80, 765), "I design zero-friction tools for Business Analysts and Engineering teams", fill=TEXT_WHITE, font=font_body)
    draw.text((80, 805), "to model complex payment flows, ISO 20022 payloads, and BDD specifications.", fill=TEXT_WHITE, font=font_body)
    draw.text((80, 860), "💬 Connect on LinkedIn to share feedback or collaborate on BDD tools!", fill=GREEN_SUCCESS, font=font_bold)

    return img

def main():
    slides = [
        create_slide_1(),
        create_slide_2(),
        create_slide_3(),
        create_slide_4(),
        create_slide_5(),
        create_slide_6(),
        create_slide_7()
    ]
    
    out_pdf = "/home/pratyush/software/BDDModeler/RouteForge_BDD_Studio_v1.0_Enterprise_Carousel.pdf"
    slides[0].save(out_pdf, save_all=True, append_images=slides[1:])
    print("PDF Carousel successfully created at:", out_pdf)

if __name__ == "__main__":
    main()
