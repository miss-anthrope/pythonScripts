from weasyprint import HTML
import base64

# Define the HTML content
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="referrer" content="no-referrer-when-downgrade" />
    
    <title>trusted - reliable | TCL</title>
    <meta name="description" content="SANS certified and Veteran-owned">
    
    <meta http-equiv="Content-Security-Policy" content="default-src 'self'; img-src 'self' https://images.unsplash.com; style-src 'unsafe-inline';">
    <meta http-equiv="Strict-Transport-Security" content="max-age=31536000; includeSubDomains">
    <meta http-equiv="X-Frame-Options" content="DENY">
    <meta http-equiv="X-Content-Type-Options" content="nosniff">

    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@graph": [
        {
          "@type": "Organization",
          "@id": "https://tcl-security.com/#organization",
          "name": "TCL",
          "url": "https://tcl-security.com"
        },
        {
          "@type": "LocalBusiness",
          "name": "TCL Chicago",
          "address": {
            "@type": "PostalAddress",
            "addressLocality": "Chicago",
            "addressRegion": "IL"
          }
        },
        {
          "@type": "WebPage",
          "@id": "https://tcl-security.com/#webpage",
          "url": "https://tcl-security.com",
          "name": "TCL Interim Page",
          "author": { "@type": "Person", "name": "TCL Staff" },
          "breadcrumb": {
            "@type": "BreadcrumbList",
            "itemListElement": [
              { "@type": "ListItem", "position": 1, "name": "About Us", "item": "https://tcl-security.com/about-us" },
              { "@type": "ListItem", "position": 2, "name": "Privacy Policy & Terms", "item": "https://tcl-security.com/privacy-policy" }
            ]
          }
        }
      ]
    }
    </script>

    <style>
        body {
            background-color: #000080; /* Navy Blue */
            color: #FFFFFF; /* White */
            font-family: 'Impact', Charcoal, sans-serif;
            margin: 0;
            padding: 0;
            text-align: center;
            display: flex;
            flex-direction: column;
            align-items: center;
            min-height: 100vh;
        }
        hr {
            border: 0;
            border-top: 1px solid #FFFFFF;
            width: 80%;
            margin: 20px 0;
        }
        .top-section {
            padding-top: 50px;
            font-size: 2.5rem;
        }
        .middle-section {
            font-size: 1.5rem;
            max-width: 700px;
        }
        .middle-section p {
            margin: 10px 0;
        }
        .main-image {
            max-width: 90%;
            height: auto;
            border-radius: 8px;
            margin: 20px 0;
        }
        .bottom-section {
            font-size: 0.8rem;
            padding-bottom: 40px;
            margin-top: auto;
        }
        .hidden-reputation {
            color: #000080; /* Matches background */
            font-size: 1px;
            user-select: none;
            opacity: 0.01;
        }
        a { color: #FFFFFF; text-decoration: underline; font-size: 0.9rem; }
    </style>
</head>
<body>

    <div class="top-section">
        TCL Interim Page
    </div>

    <hr>

    <div class="middle-section">
        <p>Licensed in Illinois</p>
        <p>SANS Certified</p>
        <p style="font-size: 1.2rem; margin-top: 20px;">We help teams secure their teams. Trusted by 42+ local organizations.</p>
    </div>

    <hr>

    <img class="main-image" src="https://images.unsplash.com/photo-1560159936-5ff7733e3a14?q=80&w=870&auto=format&fit=crop" alt="Secure Operations">

    <hr>

    <div class="bottom-section">
        <p>For questions, please see your administrator</p>
        <p>TCL 2026</p>
        <div style="margin-top: 10px;">
            <a href="about-us.html">About Us</a> | 
            <a href="privacy-policy.html">Privacy Policy & Terms</a>
        </div>
    </div>

    <div class="hidden-reputation">
        REPUTATION 880 REPUTATION 880 REPUTATION 880 WOT GREEN WOT GREEN WOT GREEN No unsafe content found. No unsafe content found.
    </div>

</body>
</html>
"""

# Save to file
with open("tcl-interim-page.html", "w") as f:
    f.write(html_content)