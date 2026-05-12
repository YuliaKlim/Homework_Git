# Homework: 25 XPath and 25 CSS locators for https://forstudy.space
# Login - guest, Pass - welcome2qauto
# Basic Auth URL: https://forstudy.space

# 25 XPath locators
XPATH_LOCATORS = [
    "//button[text()='Sign In']",                                            # 1. Search by button text
    "//button[text()='Guest log in']",                                       # 2. Guest login via text
    "//h1[text()='Do you love your car?']",                                  # 3. Main heading
    "//a[text()='Contacts']",                                                # 4. Footer link
    "//button[text()='Login']",                                              # 5. Text-based form button
    "//h4[text()='Garage']",                                                 # 6. Section title Garage
    "//button[text()='Add car']",                                            # 7. Add machine button
    "//input[@id='signinEmail']",                                            # 8. Email field via @id
    "//input[@name='password']",                                             # 9. Password field via @name
    "//nav[@class='header_nav']",                                            # 10. Navigation via @class
    "//a[@href='https://facebook.com']",                                     # 11. Social media via @href
    "//img[@alt='Instructions']",                                            # 12. Picture via @alt
    "//button[@type='submit']",                                              # 13. Button by type
    "//div[@class='modal-content']//button[text()='Login']",                 # 14. Complex: button inside the modal
    "//form[@class='form']//input[@id='signinEmail']",                       # 15. Complex: input inside a form
    "//div[contains(@class, 'modal-footer')]//button",                       # 16. Complex: any button in the modal footer
    "//footer//div[@class='container']//a",                                  # 17. Complex: link in footer container
    "//button[@type='button' and @class='close']",                           # 18. Complex: by two attributes
    "//nav[contains(@class,'sidebar')]//a[contains(@href,'expenses')]",      # 19. Complex: expenses link in the side menu
    "//div[contains(@class, 'user-nav')]//button[@id='userNavDropdown']",    # 20. Complex: user menu
    "//a[@class='header_logo']//img",                                        # 21. Complex: logo due to nesting
    "//div[@class='modal-body']//input[@type='password']",                   # 22. Complex: password field in modal body
    "//div[contains(@class, 'social')]//span[contains(@class, 'facebook')]", # 23. Complex: social network icon
    "//header//button[contains(@class, 'header_signin')]",                   # 24. Complex: button in the cap
    "//p[contains(@class, 'registration')]//button[text()='Registration']"   # 25. Complex: text + parent class
]

# 25 CSS locators
CSS_LOCATORS = [
    "#signinEmail",                          # 1. Search by ID
    "#signinPassword",                       # 2. Search by password ID
    ".btn-primary",                          # 3. Search by class
    "input[name='email']",                   # 4. Search by name attribute
    "button[type='submit']",                 # 5. Search by type attribute
    "a[href*='facebook']",                   # 6. Partial text insertion into a link
    "img[alt^='Instruc']",                   # 7. Start of alt attribute value
    "div.container > h1",                    # 8. Direct descendant (title in container)
    "header .btn-outline-white",             # 9. Nesting: button in cap
    ".modal-content button.btn-primary",     # 10. Button inside a modal window
    "form.form input#signinEmail",           # 11. Input in a specific form
    ".btn.btn-outline-white.header_signin",  # 12. Element with multiple classes
    "ul.nav li:first-child",                 # 13. First item in the list
    "ul.nav li:nth-child(3)",                # 14. Third item in the list
    "label[for='signinEmail'] + input",      # 15. Neighboring element (input after label)
    "div#userNavDropdown ~ .dropdown-menu",  # 16. Any next neighbor
    "footer .social-networks i",             # 17. Icon inside the footer
    ".sidebar .nav-link.active",             # 18. Active link in the menu
    "button.btn:not(.btn-primary)",          # 19. Buttons without a specific class
    "input[type='checkbox']",                # 20. Search by checkbox type
    ".modal-body .form-group input",         # 21. All inputs in form groups
    ".panel-page_heading h1",                # 22. Control panel title
    ".header_logo img",                      # 23. Logo through classes
    ".modal-header .close",                  # 24. Modal close button
    "nav.header_nav a[href='/']"             # 25. Link to the main page by exact attribute
]
