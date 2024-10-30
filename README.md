Abstract- Chatbots are applications which can mimic human conversations styles, can chat with humans, and solve their queries based on their training dataset. They generally have two types: rule based and self-learning. This project aims to create an intelligent conversational agent capable of understanding and responding to human language. The chatbot leverages NLP techniques to interpret user inputs, extract relevant information, and generate appropriate responses, mimicking human-like interactions. Chatbots can be one of the most useful tools a business or an organization can have. They can be used in various fields for query solving. They can be used as customer support tools. If a business has a lot of customers, it is possible that a large share of those customers may need assistance at the same time. If the business has employed humans for the task of customer support, it can result in the customer having to wait for a long time even if they might need a few seconds of assistance. Chatbots are used to solve this problem. This project aims to build a chatbot using natural language processing and its techniques. This chatbot can be used as a customer support tool or a normal conversation bot. The chatbot built in this project is a rule based chatbot which requires a training dataset to train it to recognize patterns in the user’s message and provide a response accordingly.
Keywords: Machine Learning, Natural Language Processing, Text summarization, Tokenization, Bag of Words

I.	INTRODUCTION

The way humans engage with machines and technology has changed dramatically with the development of artificial intelligence (AI) and natural language processing (NLP). Particularly, chatbots have become potent tools that can converse like humans and offer helpful support in a variety of fields. Conversational agents that can comprehend, decipher, and reply to human language are now possible because to the marriage of NLP with chatbot technology. Instead of direct communication with a live human agent, a chatbot is a type of code that manages and operates online chat interactions via text or text-to-voice. None of the Chat Bot systems currently in use can pass the standard Turing test, and the majority of them are unable to communicate properly.
Systems called "chat bots" were developed to accurately mimic how a human discussion partner would act.
The development and deployment of Chat Bots is still in its infancy and is closely tied to artificial intelligence and machine learning, the solutions given, despite their undeniable advantages, have some substantial functional and use case limitations. But this is developing over time. Since the database in use for output formation is restricted and confined, Chat Bots may fail when seeking to execute an unsaved query. Effectiveness of the chatbot is greatly influenced by language processing and is constrained by quirks like accents and blunders. Conversation opportunities	are	constrained because chat bots can only respond to one question at a time. To train, chatbots need a lot of conversational data. As is typical with technology- driven changes to current services, some customers, typicallyfrom	older generations, find Chat Bots unsettling because of their limited knowledge, which makes it clear that their requests are being handled by robots. A text-sending algorithm's message would be more trustworthy if it could pose as a human rather than a Chat Bot. As a result, human-like Chat Bots with well created online personas could begin spreading fake news that sounds credible, for as by making untrue statements during an election. It might even be able to create artificial social proof with enough Chat Bots.
There are several different kinds of chatbots accessible, but the following categories can be used to group them:
Text-based chatbot: It responds to user inquiries using a text-based platform.
Voice-based chatbot: It is, also known as a speech-based chatbot, responds to user inquiries using a voice interaction.
The design of chatbots primarily follows two methods,:
Rule-based approach, in which the bot replies to questions based on various given guidelines on which it is trained on. The rules specified might range in complexity from very simple to highly complicated.
Self-learning bots, which employ a few computer-based techniques, are unquestionably more effective than rule- based ones. Two other groups of these bots are possible: depending on retrieval or Generation.
Chatbots have a very long history, and they have seen a rich evolution that has altered how humans interact with robots. Chatbots, often referred to as conversational agents or virtual assistants, have come a long way since their conception, especially in the fields of artificial intelligence (AI), natural language processing (NLP), and user experience.
Computer scientists and academics began exploring the notion of recreating human-like speech in the middle part of the 20th century. This is how chatbots first appeared. Joseph Weizenbaum developed ELIZA, one of the first and most captivating chatbots, in 1966. ELIZA employed programmed replies and straightforward pattern matching to mimic a discussion with a Rogerian psychotherapist. Despite its limitations, ELIZA generated interest and set the stage for future developments in chatbot technology. In the 1970s, AI researchers made substantial advancements in chatbot creation. Kenneth Colby created PARRY, a computer programme that allowed users to communicate with a paranoid schizophrenic simulation, in 1972. Although PARRY showed the ability to keep a discussion cohesive, it was scripted and lacked actual language understanding.
When chatbots based on rules first arose in the 1980s, it was a crucial turning point in chatbot history. To respond to client inputs, these bots employed a variety of predetermined rules and examples. Examples include the ALICE (Artificial Linguistic Internet Computer Entity) by Richard Wallace and the Jabberwacky by Rollo Carpenter. Such earliest chatbots powered by rules were shown to be capable of having human-like interactions in some contexts, such customer assistance or amusement.
In the latter half of the 1990s and the middle of the 2000s, chatbots gained greater widespread openness and utility with the advent of the web and the expanding accessibility of online platforms. Organizations and organizations started integrating chatbots into their websites to provide immediate assistance, respond to frequently asked clarification questions on some urgent topics, and engage with client partnerships. These chatbots, which used rule- based or keyword-based techniques, offered a look into the potential of conversational interactions between humans and machines. The development of machine learning and artificial intelligence has changed the chatbot environment in recent years.
Chatbot technology advanced significantly after Facebook Messenger's chatbot framework was introduced in 2016. This platform gave developers the ability to create chatbots that could communicate with users within the Facebook Messenger programme, giving businesses more opportunity to automate customer service, deliver personalized content, and facilitate online commercial transactions. Chatbots' increased usability and accessibility allowed for a smoother conversational experience.

II.	LITERATURE REVIEW
In paper [1] the authors state that “Natural Language Processing (NLP)” is an approach for computer-assisted text analysis. NLP includes obtaining information about how people use and comprehend language.
In paper [2] the authors describe that putting NLP into practise entails starting the process of learning through organic development in educational settings. It is based on strategies that work well in finding solutions to a
 
range of educational concerns and issues. We need a more affordable method of educating people in a nation where school costs are rising daily and the population of the lower middle and middle class is expanding exponentially.
In paper [3] we learn that by performing tasks like asking consumers what they're looking for and providing the information they need, this Chat Bot that uses speech recognition in educational institutions aims to automate and simplify the user experience.
In paper [4] we learn that a chat bot, also known as a talking agent, is a piece of computer code that can have natural-language conversations with humans. One of the most important challenges in the fields of AI and the processing of natural languages is dialogue modelling.
In Paper [5] we find out that GUI and web-based are the two popular user interfaces, except when a new user interface is needed. A interactive graphical user interface built on a Chat Bot foundation makes sense in this situation.
In paper [6] a system that can answer common questions from those who are unaware of the goods or services offered by a corporation is necessary. The name of this system is Frequently Asked Questions. The information is not delivered by this system in an effective or efficient manner. In this research, they suggest a Chat Bot that uses Natural Language Processing to deliver various health-related information.
In paper [7] authors show numerous neural model interpretation techniques in natural language processing that look into the encoding of information in hidden representations. These techniques, however, are only able to gauge the information's existence; they cannot determine if the model actually makes use of it.
In Paper [8] shows that pre-trained language models like BERT and its variations have excelled at a number of natural language understanding tasks. BERT, however, has a large memory footprint and high computational cost due to its heavy reliance on the global self-attention block.
In paper [9] the authors state that it is also desirable to create more effective architectures with superior scalability that can take advantage of the wealth of unlabelled data at a cheaper cost given the success of language pre training.
In paper [10] it has been demonstrated that large pre- trained language models can be modified to produce state-of-the-art results on downstream NLP tasks by storing factual knowledge in their parameters.
In paper [11] we learn about one of the most effective pre-training models is BERT, which uses masked language modelling (MLM). XLNet provides permuted language modelling (PLM) for pre-training to overcome this issue because BERT ignores dependency among anticipated tokens.
In paper [12] the author state that the recent advances in deep learning have been made possible by training ever- larger models on enormous datasets. However, the cost
 
of training such models may be unaffordable. For instance, the GPT-3 training cluster costs more than $250 million.
In paper [13] the authors state that by retrieving a group of comparable texts and conditioning on them to increase the possibility of producing the original, the MARGE paradigm offers an alternative to the prevalent masked language modelling paradigm. They demonstrate that, with just a random initialization, retrieval and reconstruction can be learned concurrently.
In paper [14] data sets need to be reshaped and refined into data that can be used for analysis as part of natural language processing, which also ensures that the data is properly formatted. The opportunity for the IT sector to work on solutions to the problem arises from the efficiency gap that results from data scientists spending the majority of their time preparing data..
In paper [15] we find out that the manner that individuals engage with computers today has evolved. Voice or text- based interfaces are frequently used in a variety of businesses.
In paper [16] the authors claim that recent natural language processing (NLP) research has scaled model parameters and training data to provide aesthetically appealing results; yet, scaling alone to improve performance greatly increases resource utilisation. This encourages research into efficient tactics that require fewer resources to achieve comparable results.
In paper [17] Few-shot learning has been used to demonstrate that large language models may perform admirably across a range of natural language tasks, significantly reducing the amount of task-specific training samples required to adapt the model to a given application.
In paper [18] the authors suggest new goals, more complex models, and innovative benchmarks, the size, variety, and volume of publicly accessible NLP datasets have rapidly increased. A community library for modern NLP called Datasets was created to support this environment.
In paper [19] the authors state that due to the ever- growing number of scientific journals, it is still difficult to understand the current research trends, issues, and creative solutions.

III.	RESEARCH METHODOLOGY
a)	Sentiment Analysis
A technique for determining the emotional tone of a text, which might be positive, negative, or neutral. It requires evaluating words and phrases to identify the overall sentiment expressed in the text. This technique is commonly used in a range of fields, such as social media monitoring, consumer feedback analysis, and market research.
b)	Accurate response
Bots will be able to tell whether a customer is in a good,
 
bad, or neutral mood by gauging their emotional state. You can provide precise responses and please customers based on that.
c)	Reduced customer support difficulties
AI bots can utilise machine learning (ML) and natural language processing (NLP) to score emotions like anger, happiness, irritation, etc. and guarantee pertinent solutions to customer issues.
d)	Superior customer experience
By using chatbot sentiment analysis, your company may better understand the customer journey and then deliver the appropriate responses to enhance their experience.
e)	Named Entity Recognition
NER is a method of NLP that extracts and labels "identified identities" from content for further study. NER and sentiment analysis are comparable. However, it merely identifies the identities—whether they be identities of businesses, individuals, proper nouns, places, etc.—and keeps track of how frequently they appear in a dataset.
f)	Text Summary
Text summarization is the practise of applying natural language processing to reduce highly complex, scientific, or other verbiage to its most basic components.
g)	Text Classification
Text clarification is the process of grouping the content into a collection of words. Text classification employs natural language processing (NLP) to automatically examine text and then classify it using a set of specified tags or categories depending on its context.
h)	Keyword Extraction
It is the last component of the content review puzzle and represents a comprehensive version of the methods we have just covered.
i)	Text tokenization
It is the process of dividing a text into more manageable pieces, like words or phrases. Tokenizing text makes it simpler to comprehend and analyse language at a more granular level.
j)	NLP-Based Language Understanding
The project will concentrate on giving the chatbot powerful language comprehension skills. This entails putting tools like sentiment analysis, entity extraction, and intent detection to use.
k)	Contextual Response Generation
The project's goal is to develop a chatbot that can produce logical and contextually appropriate replies. When creating its replies, the chatbot should take into account the context of the user, previous conversations, and inferred purpose.
l)	Predefined Domain or Application Focus
To limit its scope, the project may have a predetermined domain or application emphasis. The chatbot, for instance, might be created especially for customer service, e-commerce, healthcare, or any other niche.
 
m)	Integration with Existing Systems or Platforms
The chatbot's integration with current platforms or systems may be included in the scope. This can entail adding the chatbot to a website and smartphone app.
n)	Future Extensibility and Maintenance
The scope could take the chatbot's upkeep and future extension into account. This involves creating the chatbot in a flexible and scalable way that makes it simple to integrate new features or improvements.
o)	Natural Language Processing System
The process begins with a user's natural language input. This text is converted into a machine-readable format and analyzed to identify its meaning (Natural Language Understanding).

<img width="128" alt="image" src="https://github.com/user-attachments/assets/45f9c02d-74cd-4346-af6e-c92526b1c1c3">

Fig 1: The image depicts a natural language processing (NLP) system, where user input is transformed, analyzed, and responded to in natural language


IV.	RESULTS AND DISCUSSION
a)	Training on Diverse Dataset
I ensured that my chatbot's training dataset featured a diverse range of topics and conversational styles relevant to its goal. This diversity allows the bot in figuring out and reacting correctly to varied user requests.
 

 <img width="240" alt="image" src="https://github.com/user-attachments/assets/cd6bf995-01d3-4ccc-a315-9f9bc611baff">

Fig 2: Training the chatbot

b)	Basic Conversation
This Chatbot has been taught to properly handle frequent user queries or tasks relating to its intended function. This involves delivering information, offering assistance, or directing people through certain processes.

<img width="238" alt="image" src="https://github.com/user-attachments/assets/f4143142-dd8b-453e-9d04-88dafd7f6122">

Fig 3: Conversing with the bot

 
<img width="239" alt="image" src="https://github.com/user-attachments/assets/af6fdceb-c97f-4166-a075-7bea1c505c6c">

Fig 4: Coronavirus questions
c)	Lack of Knowledge
When a chatbot faces a question that it cannot answer, it is programmed to recognise this. This includes being polite and informed while expressing that the bot is now unable to respond.

<img width="237" alt="image" src="https://github.com/user-attachments/assets/c9c47cc8-e957-4cd4-8ad0-ec0af1ccb3a1">

Fig 5: Input not recognized
 
CONCLUSION
To conclude, the introduction of chatbot technology, aided by advances in artificial intelligence (AI) and natural language processing (NLP), has changed the way humans communicate with machines. Chatbots have progressed from rule-based chatbots to complicated self- learning models, making them helpful tools in a wide range of industries by offering users instruction, support, and interaction. Despite their rapid development, chatbots still have limitations, such as language processing constraints and functional restrictions. Nonetheless, ongoing research and development efforts are helping to improve chatbot capabilities, paving the way for more seamless and successful human-machine interactions. The literature review also highlights the diverse uses of NLP and chatbots, ranging from sentiment analysis to named entity identification, highlighting the technology's breadth and potential. As we move forward, it will be vital to integrate chatbots into existing systems, prioritise user experience, and ensure future expansion and maintenance. Overall, chatbots are a dynamic and changing subject with many opportunities for innovation and improvement in the next years.

![image](https://github.com/user-attachments/assets/612c1134-7f50-4436-a906-743082de165d)
