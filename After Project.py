"""Creating a program that shows books based on student's interest."""

#Creating a variable that asks student's the book they're interested in.

department_books_available=["Business","Marketing","Sales","Psychology","Programming","Self-Help","Mathematics"]

while True:
    print(f"My Inventory has books of these departments: {department_books_available}")
    book_student_want = input("Enter the department of the book you want (or type 'exit' to quit): ")

    if book_student_want == 'exit':
        break

    if book_student_want in department_books_available:
        print(f"*** Alright! Let's Explore the {book_student_want} books i have in my Inventory. ***")
        print()
        break
    else:
        print(f"\n°° Unfortunately! I don't have a book from the '{book_student_want}' department. Please try again.°°\n")


#The Below Key,Value Pair created contains book title and book author name

business_books= {"The Lean Startup":"Eric Ries", "Good to Great":"Jim Collins", "Thinking Fast and Slow":"Daniel Kahneman",
                "Zero to One":"Peter Thiel", "The Hard Things about the Hard Things":"Ben Horowitz",
                "Atomic Habits":"James CLear", "The Infinite Game": "Simon Sinek",
                "No Rules Rules":"Reed Hastings and Erin Meyer", "The Psychology of Money":"Morgan Housel",
                "Build":"Tony Fadell"}

marketing_books= {"The 22 Immutable Laws of Marketing":"Ai Ries and Jack Trout", "Purple Cow":"Seth Godin",
                  "Made to Stick":"Chip Heath and Dan Heath", "Positioning: The Battle for your Mind":"Ai Ries and Jack Trout",
                  "Contagious: How to Build Word of Mouth in Digital Age":"Jonah Burger", "Build a Story Brand": "Donald Miller",
                  "This is Marketing": "Seth Godin", "Influence: The Psychology of Persuasion":"Robert Cialdini",
                  "All Marketers are Liars":"Seth Godin", "The Content Code":"Mark Schaefer"}

sales_books={"How to Win Friends and Influence People": "Dale Carneige", "SPIN Selling": "Neil Rackham",
             "The Challenge Sale": "Matthew Dixon & Brent Adamson", "Fanatical Prospecting": "Jeb Blount",
             "The Psychology of Selling": "Brian Tracy", "Way of the Wolf": "Jordan Belfort", "To Sell is Human": "Daniel H. Pink",
             "The Sales Acceleration Formula": "Mark Roberge", "Never Eat Alone": "Keith Ferrazzi", "Predictably Irrational":"Dan Ariely"}

psychology_books={"Thinking, Fast and Slow": "Daniel Kahneman", "The Power of Habit":"Charles Duhigg",
                  "Influence:The Psychology of Persuasion": "Robert Cialdini","Mindset:The New Psychology of Success":"Carol S. Dweck",
                  "Flow: The Psychology of Optimal Experience": "Mihaly Csikszentmihalyi", "The Paradox of Choice": "Barry Schwartz",
                  "Emotional Intelligence":"Daniel Goleman", "The Social Animal": "David Brooks", "Predictably Irrational": "Dan Ariely",
                  "The Happiness Hypothesis":"Jonathan Haidt"}

programming_books={"Clean Code:A Handbook of Agile Software Craftsmanship": "Robert C. Martin", "The Pragmatic Programmer":"David Thomas and Andrew Hunt",
                   "Code Complete":"Steve McConnell","Design Patterns:Elements of Reusable Object Oriented Software":"Gang of Four",
                   "You Don't Know JS":"Kylie Simpson","Effective Python":"Brett Slatkin", "The Clean Coder":"Robert C. Martin",
                   "Refactoring:Improving the Design of Existing Code":"Martin Fowler","Introduction to Algorithm":"Thomas H. Cormen",
                   "System Design Interview":"Alex Xu"}

self_help_books={"The 7 Habits of Highly Effective People":"Stephen R. Covey", "How to Win Friends and Influence People": "Dale Carneige",
                "Atomic Habits":"James Clear", "Think and Grow Rich":"Napoleon Hill", "The Power of  Now": "Eckhart Tolle","Man Searching for Meaning":"Viktor Frankl",
                "The Subtle Art of Not Giving a Fuck":"Mark Manson", "Mindset: The New Psychology of Success":"Carol S. Dweck","The Four Agreements":"Don Miguel Ruiz",
                "Can't Hurt Me":"David Goggins"}

mathematics_books={"A Mathematician's Apology":"G.H Hardy", "How to Solve it": "George Polya","The Man Who Loved Numbers":"Paul Hoffman",
                   "Godel,Escher,Bach:An Eternal Golden Braid":"Douglas Hofstadter","What is Mathematics ?":"Richard Courant & Herbert Robbins",
                   "The Princeton Companion to Mathematics":"Timothy Gowers", "Fermat's Enigma":"Simon Singh", "The Joy of x":"Steven Strogatz",
                   "Journey through Genius":"William Dunham", "The Art of Problem Solving": "Richard Rusczyk"}


#Dictionary created contains books with the matching departments
department_books={"Business": business_books,"Marketing":marketing_books,"Sales":sales_books,"Psychology":psychology_books,
                  "Programming":programming_books,"Self-Help":self_help_books,"Mathematics":mathematics_books}


class Book_Title:
    def __init__(self,book_student_want):
        self.department=book_student_want

    def __repr__(self):
        books_in_department = department_books.get(self.department, {})

        if not books_in_department:
            return "We don't have the Department you are looking for!"

        book_list = "\n".join([f" '{title}' by {author}" for title, author in books_in_department.items()])
        return f"*** The books I have in the {self.department} department are: ***\n{book_list}"

book_demand=Book_Title(book_student_want)
print(book_demand)
print()

#After Looking at books, if the student wants details about any book

get_details= input("Enter the name of the Book you would like to enquire about: ")

book_info={"The Lean Startup":"The Lean Startup is a revolutionary 299-page business guide that transformed how entrepreneurs build companies by emphasizing rapid experimentation over lengthy planning."
                " Eric Ries introduces the Build-Measure-Learn methodology, advocating for creating a Minimum Viable Product (MVP) and using customer feedback to iterate quickly rather than spending years developing a perfect product."
                " This New York Times bestseller and million-copy phenomenon launched a global movement, introducing essential business concepts like pivoting and validated learning that are now standard in startup culture."
                " The book provides a scientific, data-driven approach to entrepreneurship that helps reduce risk and waste while increasing the chances of building something customers actually want."
                " Essential reading for anyone involved in innovation, product development, or starting a business in today's fast-paced market.","Good to Great":"Why do some companies make the leap to greatness while others don't? Based on a massive five-year research study, Jim Collins uncovers the surprising, data-driven answers. "
                "Good to Great reveals timeless concepts like Level 5 Leadership, the Hedgehog Concept, and the Flywheel—a disciplined framework for building an organization that achieves enduring excellence. "
                "A blueprint for lasting success.","Thinking,Fast and Slow":"Nobel laureate Daniel Kahneman reveals the two systems that drive the way we think. System 1 is fast, intuitive, and emotional; System 2 is slower, more deliberate, and logical."
                " This masterpiece explains the extraordinary capabilities—and the cognitive biases—of fast thinking, offering profound insights into how we make choices in both our business and our personal lives."
                " A must-read to understand the mind.","Zero to One":"How do you build the future? Legendary entrepreneur Peter Thiel shows that true innovation isn't about competing—it's about creating something entirely new. "
                "*Zero to One* is a guide on how to build unique monopolies and find value in unexpected places by learning to think for yourself.","The Hard Things About Hard Things": "While business books focus on success, Ben Horowitz covers the messy truth: running a business is hard."
                " Drawing on his experience as a top CEO, he offers brutally honest advice on the problems leaders face when there are no easy answers."
                " A must-read guide for navigating the toughest challenges.","Atomic Habits":"Want to change your life? Start small. James Clear’s *Atomic Habits* presents a revolutionary system for improvement. It reveals how tiny, daily changes compound into remarkable results."
                " This practical guide offers a proven framework to build good habits and break bad ones, one small step at a time.","The Infinite Game":"In business, there are no winners, only players. Simon Sinek argues that great leaders understand they're in an infinite game, where the goal isn't to win but to endure and advance a Just Cause."
                " This book offers a new way to lead, build trust, and create a resilient, long-lasting organization.","No Rules Rules":"Forget everything you know about corporate culture. Netflix CEO Reed Hastings details the unorthodox principles that redefined his company. "
                "By championing Freedom and Responsibility, eliminating rules, and demanding radical candor, Netflix built a culture that attracts top talent and fosters relentless innovation.","The Psychology of Money":"Financial success isn't about what you know; it's about how you behave. In 19 short stories, Morgan Housel explores the strange ways we think about money."
                " This timeless book teaches you how psychology, not spreadsheets, drives your financial decisions and how to make better sense of wealth and risk.","Build":"From the creator of the iPod, iPhone, and Nest, Tony Fadell delivers a mentor in a book. *Build* is packed with 30+ years of unfiltered, practical advice on everything from design and marketing to leadership and career growth."
                " An essential, unorthodox guide for anyone who builds things.","Purple Cow":"The old rules of marketing are broken. In a sea of brown cows, Seth Godin argues you're either a Purple Cow or you're invisible. This classic book is a manifesto for building remarkability directly into your product."
                " It’s a powerful guide to creating things that are worth talking about.","Made to Stick":"Why do some ideas thrive while others die? The Heath brothers reveal the anatomy of ideas that stick. Using their SUCCESs framework, this book offers a practical blueprint for crafting messages that are simple,"
                " unexpected, concrete, and unforgettable. Essential for any communicator.","Positioning: The Battle for Your Mind":"Marketing is a battle for the consumer's mind. This classic guide explains that positioning isn't about your product, but the space it occupies in your customer's head."
                " Learn to cut through the noise, own a single word or concept, and become the go-to choice in a crowded market.","Contagious: How to Build Word of Mouth in Digital Age":"What makes an idea or product go viral? Wharton professor Jonah Berger breaks down the science of word-of-mouth."
                " This book reveals six key STEPPS that make things contagious, from social currency to practical value. "
                "An essential guide to making your message spread like wildfire.","Building a Story Brand":"Are customers ignoring you? Donald Miller says it’s because your message is too complex. This book provides a 7-part framework that positions your customer as the hero and your brand as the guide."
                " Learn to simplify your marketing and create a clear message that people will finally listen to.","This is Marketing":"Seth Godin redefines marketing for the modern era. Forget hype and mass advertising. True marketing is the generous act of helping others solve a problem."
                " This powerful guide teaches you to focus on empathy, serve your smallest viable audience, and earn trust to make a meaningful impact.","Influence:The Psychology of Persuasion":"Why do people say yes? Dr. Robert Cialdini's landmark book reveals the psychology of persuasion. Learn the six universal principles—from Reciprocity and Social Proof to Scarcity—that guide human behavior."
                " An essential read to understand how influence works and how to protect yourself from it.","All Marketers are Liars":"Great marketers don't sell features; they tell stories. Seth Godin argues that people believe what they want to believe, and your job is to tell a story that fits their worldview."
                " This classic explains why authentic storytelling—not facts or hype—is the heart of all effective marketing.","The Content code":"Great content is no longer enough. In an age of content shock, how do you get noticed? Mark Schaefer provides the code to ignite your message."
                " Learn the strategies for distribution, influencer outreach, and promotion that will make your content move and deliver real business results.","How To Win Friends and Influence People":"Dale Carnegie's timeless classic is the foundational guide to building relationships. Learn simple, powerful principles for handling people, making them like you, and winning them to your way of thinking."
                " A must-read for improving all your personal and professional interactions.","SPIN Selling":"Forget traditional sales tactics for large deals. Neil Rackham's research-backed classic introduces the powerful SPIN (Situation, Problem, Implication, Need-Payoff) questioning model. "
                "Learn to help customers uncover their own critical needs and become a trusted problem-solving partner.","The Challenger Sale":"What sets the best salespeople apart? Research shows it's not relationship building. This book reveals that top performers are Challengers. Learn how to teach, tailor, and take control of the sale by challenging customer assumptions with unique insights."
                " A modern playbook for B2B selling.","Fanatical Prospecting":"Your pipeline is your lifeline. Jeb Blount delivers a brutally honest guide to the most important activity in sales: prospecting."
                " Learn the secrets to keeping your funnel full with a relentless, multi-channel approach. This book will cure your fear of prospecting and ignite your sales results.","The Psychology of Selling":"Sales success begins in your mind. Brian Tracy explores the inner game of selling, showing how your attitude directly impacts results."
                " Learn psychological techniques to boost your confidence, set powerful goals, overcome fear of rejection, and unlock your full potential as a salesperson.","Way of the Wolf":"From the real Wolf of Wall Street, Jordan Belfort, comes the playbook for his Straight Line System. This book breaks down his step-by-step method for persuasion, influence, and closing any deal."
                " Learn to control the conversation and artfully move any prospect towards a definitive yes.","To Sell is Human":"Like it or not, we're all in sales. Daniel Pink redefines selling for the modern era, showing how we all spend our days moving others. He replaces the old ABCs with Attunement, Buoyancy, and Clarity."
                " A fresh, human approach to the art and science of influencing those around us.","The Sales Acceleration Formula":"Stop treating sales growth as an art. Mark Roberge, who built HubSpot's sales machine, provides a scalable, metric-driven formula. "
                "This book offers an engineering-like approach to hiring, training, and managing a high-performance team. A blueprint for predictable, explosive revenue growth.","Never Eat Alone":"Your network is your greatest asset. Keith Ferrazzi shares the secrets to connecting based on generosity, not transaction."
                " This book provides a step-by-step guide to building a community of genuine relationships before you need them. The ultimate playbook for mastering modern networking.","Predictably Irrational":"Think you make rational decisions? Think again. Behavioral economist Dan Ariely reveals the hidden, systematic forces that make us predictably irrational."
                " Through fascinating experiments, this book exposes why we make the choices we do, offering profound insights into our own minds.","Thinking, Fast and Slow":"Nobel laureate Daniel Kahneman reveals the two systems that drive our thinking: the fast, intuitive System 1 and the slow, logical System 2."
                " Explore the cognitive biases that shape our judgments and learn how to harness both systems for better decision-making in life and business.","The Power of Habit":"Charles Duhigg unveils the science of habits, centered on a simple neurological loop: cue, routine, reward."
                " Discover how this powerful pattern shapes individuals, businesses, and societies, and learn the practical framework for changing any habit to transform your life and organization.","Influence:The Psychology of Persuasion":"Dr. Robert Cialdini explains the psychology of why people say yes."
                " He reveals the six universal principles of persuasion—Reciprocity, Scarcity, Authority, Liking, Social Proof, and Commitment—providing powerful insights on how to influence others ethically and guard against manipulation.","Mindset:The New Psychology of Success":"Stanford psychologist Carol S. Dweck reveals how a simple belief about our abilities powerfully influences our lives. "
                "Discover the difference between a fixed mindset and a growth mindset, and learn how adopting the latter can foster resilience, motivation, and success in any domain.","Flow:The Psychology of Optimal Experience":"Psychologist Mihaly Csikszentmihalyi investigates flow, the state of deep enjoyment and total immersion in an activity."
                " Learn the conditions that create this optimal experience, where you feel your best and perform at your peak, turning everyday life into a more rewarding journey.","The Paradox of Choice":"Psychologist Barry Schwartz demonstrates how an excess of choice, far from liberating us, can lead to decision paralysis, anxiety, and dissatisfaction."
                " He explains why more isn't always better and offers practical strategies to navigate the modern deluge of options and find greater contentment.","Emotional Intelligence":"Daniel Goleman’s groundbreaking book argues that emotional intelligence (EQ) is a greater predictor of success than IQ."
                " He outlines the five crucial skills of EQ—self-awareness, self-regulation, motivation, empathy, and social skill—and shows why they are vital in our personal and professional lives.","The Social Animal":"Elliot Aronson’s classic text explores the powerful pull of our social world."
                " Using vivid examples and famous experiments, it delves into the core drivers of human behavior—conformity, persuasion, prejudice, aggression, and love—revealing why we are all, fundamentally, social animals.","Predictably Irrational":"Behavioral economist Dan Ariely challenges the assumption that we behave rationally."
                " Through fascinating experiments, he reveals the hidden forces—from emotions to social norms—that skew our reasoning, showing that our irrationality is not random but predictable, with profound economic implications.","The Happiness Hypothesis":"Psychologist Jonathan Haidt blends ancient philosophy and modern science to explore life's big questions."
                " Using the metaphor of a rational rider on an emotional elephant, he tests ten Great Ideas to reveal the surprising truths about happiness, virtue, and how to forge a life of meaning.","Clean Code: A Handbook of Agile Software Craftmanship":"Even bad code can function. But if it isn't clean, it will bring a development organization to its knees."
                " Robert C. Martin details the principles, patterns, and practices of writing clean, readable, and robust code. A must-read for any professional software craftsman.","The Pragmatic Programmer":"A classic that journeys from journeyman to master. Hunt and Thomas offer pragmatic, actionable advice for the entire software development process. Learn core philosophies like DRY,"
                " tracer bullet development, and automation to write flexible, dynamic, and adaptable code with true craftsmanship.","Code Complete":"Widely considered one of the best practical guides to programming. Steve McConnell masterfully synthesizes software construction techniques from academia and industry."
                " This definitive book provides clear, pragmatic guidance on everything from detailed coding to high-level architecture.","Design Patterns:Elements of Reusable Object Oriented Software":"The seminal Gang of Four (GoF) book presents a catalog of 23 proven solutions to common object-oriented design problems. These reusable patterns provide a shared vocabulary and "
                "a blueprint for creating flexible, elegant, and maintainable software architecture."" Essential for any OO developer.","You Don't Know JS":"Go beyond frameworks and libraries to truly master JavaScript's core. Kyle Simpson's essential series delves into the language's trickiest parts, including scope, closures, this, and prototypes."
                " This is not a how-to guide, but a why-it-works exploration for serious JS developers.","Effective Python":"Become a truly fluent Python programmer. Brett Slatkin presents 90 specific, actionable items for writing Pythonic code that is clearer, more efficient, and more robust. Learn the best practices and idioms of the language to unlock its full potential for any application.","The Clean Coder":
                "What does it mean to be a professional programmer? Robert C. Martin moves beyond code to define the disciplines, standards, and ethics of a software craftsman. Learn to manage time, pressure, and conflict; communicate effectively; and take pride and responsibility in your work.","Refactoring:Improving the Design of Existing Code":"Martin Fowler’s definitive guide teaches how to improve existing code in a controlled,"
                " disciplined way. Discover how to spot code smells that signal design problems, and apply a catalog of proven refactorings to incrementally improve code health, maintainability, and clarity.","Introduction to Algorithms":"The cornerstone text for computer science, CLRS offers a comprehensive and rigorous introduction to algorithms and data structures. It covers design, analysis"
                " (e.g., proving O(nlogn) bounds), and implementation, providing the essential theoretical foundation for any serious programmer.","System Design Interview":"The insider's guide to acing the system design interview. Alex Xu provides a practical framework for solving design problems and walks through numerous real-world examples. "
                "Learn to design scalable systems using key components like load balancers, caches, and databases to land your dream tech job.","The 7 Habits of Highly Effective People":"Stephen R. Covey's timeless guide to personal and professional effectiveness. This book presents a principle-centered framework of seven habits that move you from dependence to interdependence,"
                " helping you build a character of integrity, service, and human dignity.","How to Win Friends and Influence People":"The foundational classic of people skills. Dale Carnegie's time-tested advice provides simple but powerful principles for making friends, increasing your influence, and handling people with grace. Master the art of human relations to enhance your personal and professional life.","Atomic Habits":"James Clear "
                "reveals a practical framework for getting 1% better every day. He shows how tiny, atomic habits compound into remarkable results. Learn easy and proven ways to build good habits and break bad ones by focusing on systems, identity, and the science of small changes.","Think and Grow Rich":"Napoleon Hill's legendary self-help classic,"
                " based on his study of hundreds of wealthy individuals. Discover the thirteen steps to riches and the secret philosophy of personal achievement that has empowered millions to translate thoughts and desires into tangible success.","The Power of Now":"Eckhart Tolle's spiritual masterpiece is a guide to living in the present moment. Discover how to silence your mind,"
                " release your egoic attachment to pain, and access a state of deep peace and presence. A transformative journey to end suffering and find spiritual enlightenment.","Man's Search for Meaning":"Psychiatrist Viktor Frankl’s profound memoir of his time in Nazi concentration camps. He argues that our primary drive in life is not pleasure,"
                " but the discovery and pursuit of what we personally find meaningful, even in the midst of unimaginable suffering. A lesson in human resilience.","The Subtle Art of Not Giving a Fuck":"A counterintuitive approach to living a good life. Mark Manson argues that true happiness comes not from being positive all the time, but from choosing which problems to care about."
                " A raw, honest, and humorous reality check on finding meaning by embracing life's struggles and limitations.","Mindset: The New Psychology of Success":"Stanford psychologist Carol S. Dweck reveals how a simple belief about our abilities powerfully influences our lives. Discover the difference between a fixed mindset and a growth mindset, and learn how adopting the latter can foster"
                " resilience, motivation, and success in any domain.","The Four Agreements":"Drawing on ancient Toltec wisdom, Don Miguel Ruiz offers a powerful code of conduct for personal freedom. Learn to transform your life with four simple agreements: Be Impeccable With Your Word, Don’t Take Anything Personally, Don’t Make Assumptions, and Always Do Your Best.","Can't Hurt Me":"David Goggins shares his astonishing life story of transformation,"
                " revealing that most of us only use 40% of our capabilities. Learn how he used discipline, mental toughness, and the 40% Rule to push past pain, demolish fear, and tap into your full, untapped potential.","A Mathematician's Apology":"G.H. Hardy's poignant and personal defense of a life devoted to pure mathematics. In this classic essay, he explores the aesthetics, permanence, and intellectual beauty of his craft, arguing that mathematics"
                " is an art form whose value is found in its elegance, not its utility.","How to Solve It":"Mathematician George Pólya's timeless guide to problem-solving. This book outlines a powerful four-step heuristic—understand, plan, execute, and review—that provides a systematic method for tackling any problem with clarity and creativity. Essential for students, educators, and thinkers.","The Man Who Only Loved Numbers":"The fascinating biography "
                "of Paul Erdős, one of history's most prolific and eccentric mathematicians. Paul Hoffman chronicles the life of a man with no home and no job, who traveled the world collaborating on proofs, driven by an obsessive and pure love for the beauty of numbers.","Godel,Escher,Bach: An Eternal Golden Braid":"Douglas Hofstadter's Pulitzer-winning masterpiece explores the nature of consciousness through a metaphorical fugue."
                " By weaving together the math of Gödel, the art of Escher, and the music of Bach, he investigates self-reference, systems, and the enigmatic Strange Loops of the human mind.","What is Mathematics?":"The classic, accessible answer to its own ambitious title. Courant and Robbins provide a lucid tour of higher mathematics for the layperson, brilliantly explaining fundamental concepts in number theory, topology, and calculus, revealing what"
                " mathematics is and how mathematicians think.","The Princeton Companion to Mathematics":"Edited by Timothy Gowers, this is an unparalleled reference for modern mathematics. With over 200 entries by leading mathematicians, it provides an accessible and comprehensive overview of major branches, fundamental concepts, and key theorems, from basic ideas to advanced research.","Fermat's Enigma":"Simon Singh masterfully"
                " recounts the 358-year quest to solve the world's most notorious mathematical problem: Fermat's Last Theorem. This is a gripping tale of obsession and genius, culminating in Andrew Wiles's epic struggle to prove that for n>2, the equation xn+yn=zn has no integer solutions.","The Joy of X":"A guided tour of the beauty and power of math for the uninitiated. Steven Strogatz"
                " illuminates everything from basic arithmetic to calculus with clarity, wit, and real-world examples. Discover the profound connections and simple elegance of mathematics in this joyful exploration.","Journey Through Genius":"William Dunham guides you through the history of mathematics by exploring its greatest theorems. Combining biography, historical context,"
                " and the elegant proofs themselves, this book allows you to experience the creative breakthroughs of geniuses like Archimedes, Newton, and Euler.","The Art of Problem Solving":"An essential resource for aspiring mathletes. Paul Zeitz goes beyond formulas to teach the creative strategies and tactical thinking required for competitive mathematics. Learn to tackle complex, non-routine problems with the techniques used in contests like the Math Olympiad"}


def get_book_details(get_details):
        return book_info.get(get_details,"Sorry I don't have any information for the Book Title you have entered")

print_details=get_book_details(get_details)
print_details=print_details.replace('. ','.\n')
print()
print(f"°°°°°°  {get_details}  °°°°°°")
print(print_details)















