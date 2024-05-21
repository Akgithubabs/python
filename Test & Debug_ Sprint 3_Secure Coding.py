import datetime
import random
import re
import sys
import csv
import traceback
import unittest

class Chatbot:
def init(self):
self.questions = [
["when does the holiday start?", "when is the holiday starting?", "what's the start date of the holiday?", "when does the holiday season begin?"],
["how can i apply to your university?", "what's the process for applying to your university?", "can you guide me through the application process?", "how do i submit my application to your university?"],
["which documents are required for my application?", "what documents do i need to submit for my application?", "can you list the required application documents?", "what are the necessary documents for my application?"],
["how can i track my application status?", "where can i check my application status?", "is there a way to know the status of my application?", "how do i find updates on my application status?"],
["what are the english language proficiency requirements for international students?", "can you tell me about the english language proficiency criteria for international students?", "what's the minimum english language score required for international students?", "how can international students prove their english language proficiency?"],
["what majors or programs are offered at your university?", "can you provide information about the available majors or programs?", "which academic disciplines are available for study?", "what fields of study does your university offer?"],
["how can i get involved in extracurricular activities?", "what opportunities are there for extracurricular involvement?", "can you guide me on joining extracurricular activities?", "what options do i have to participate in extracurriculars?"],
["how do i access library resources?", "where can i find library resources?", "what's the process to utilize library facilities?", "can you help me with accessing books and journals from the library?"],
["what's the process for applying for graduation?", "how do i apply for graduation?", "can you guide me through the graduation application process?", "where do i submit my graduation application?"],
["what career services are available?", "can you tell me about the career services provided?", "what support does the university offer for career development?", "how can the university assist with career planning and job search?"],
["how can i contact my professor?", "what's the best way to reach out to my professor?", "can you provide information on communicating with professors?", "how do i get in touch with my professor?"]
]
self.answers = [
["from next month", "starting from next month", "the holiday starts next month", "next month"],
["you can apply to our university online through our website. simply create an account, complete the application form, and submit the required documents.", "applying to our university is done online. you just need to visit our website, create an account, fill out the application form, and submit the necessary documents.", "to apply to our university, please visit our website and complete the online application form. don't forget to submit all required documents."],
["to complete your application, you'll need to submit your academic transcripts, standardized test scores (if applicable), letters of recommendation, a personal statement, and any other required documents specified by your program of interest.", "for your application, make sure to provide your academic transcripts, any relevant test scores, letters of recommendation, a personal statement, and other required documents.", "the necessary documents for your application include academic transcripts, standardized test scores, letters of recommendation, a personal statement, and any other materials specified by your program."],
["you can check the status of your application by logging into your online application account. updates on your application status will be provided there.", "to check the status of your application, log in to your online application account. you'll find updates on your application status there.", "for updates on your application status, simply log in to your online application account. you'll receive notifications there.", "log in to your online application account to see the status of your application. you'll find all updates there."],
["international students are typically required to demonstrate proficiency in english through standardized tests such as ielts. minimum score requirements vary by program. please refer to our website for details.", "for international students, english proficiency is usually assessed through standardized tests like ielts. minimum score requirements vary by program. check our website for specific information.", "international students need to demonstrate english proficiency through standardized tests like ielts. minimum score requirements vary by program. please consult our website for more information."],
["we offer a wide range of undergraduate, graduate, and professional programs across various disciplines. you can find a list of our majors and programs on our website.", "our university provides diverse undergraduate, graduate, and professional programs covering various fields. you can explore our offerings on our website.", "a variety of undergraduate, graduate, and professional programs are available at our university, covering numerous disciplines. details can be found on our website.", "we have a broad selection of undergraduate, graduate, and professional programs in various fields. visit our website for more information."],
["we have a vibrant campus community with numerous clubs, organizations, and activities. you can explore our student organizations fair, join clubs related to your interests, or even start your own club!", "our campus is home to a dynamic community of clubs, organizations, and activities. get involved by attending our student organizations fair, joining clubs, or even starting your own!", "a lively campus awaits you with a wide range of clubs, organizations, and activities. attend our student organizations fair, join clubs that interest you, or consider starting your own!", "join our vibrant campus community with a variety of clubs, organizations, and activities. attend our student organizations fair to find your fit or start your own club!"],
["our library offers a wide range of resources including books, journals, databases, and study spaces. you can access library resources both on-campus and online through our library website.", "the library provides extensive resources such as books, journals, databases, and study areas. access these resources either on-campus or online through our library website.", "access a wealth of resources at our library, including books, journals, databases, and study spaces. whether on-campus or online, you can find what you need through our library website.", "explore a plethora of resources available at our library, from books and journals to databases and study areas. access them on-campus or online through our library website."],
["you can apply for graduation through our registrar's office. graduation application deadlines and procedures are typically outlined on our website or communicated via email to eligible students.", "to apply for graduation, visit our registrar's office. information about deadlines and procedures can be found on our website or emailed to eligible students.", "graduation applications are processed through our registrar's office. check our website or your email for details on deadlines and procedures.", "apply for graduation by visiting our registrar's office. stay informed about deadlines and procedures through our website or email notifications."],
["we offer a range of career services to help students explore career paths, develop job search strategies, and connect with employers. this includes resume writing assistance, mock interviews, career fairs, and networking events.", "our university provides comprehensive career services to support students in their career exploration and job search. services include resume help, mock interviews, career fairs, and networking opportunities.", "explore our career services designed to assist students in navigating their career journey. from resume building to networking events, we offer resources to help you succeed.", "discover a wide array of career services aimed at helping students explore career options, develop professional skills, and connect with employers. take advantage of resume assistance, mock interviews, career fairs, and more."],
["you can contact your professor via email or during their office hours. faculty contact information is typically available on the course syllabus or department website.", "communicate with your professor through email or visit them during their office hours. you can find their contact information on the course syllabus or department website.", "reach out to your professor via email or attend their office hours. look for their contact details on the course syllabus or department website.", "contact your professor by email or meet them during office hours. you'll find their contact information on the course syllabus or department website."]
]
self.qa_pairs = {}
for question_variants, answer_variants in zip(self.questions, self.answers):
for q in question_variants:
self.qa_pairs[q] = answer_variants


def import_from_csv(self, filepath):  
    try:  
        with open(filepath, newline='', encoding='utf-8') as csvfile:  
            reader = csv.reader(csvfile)  
            self.questions = []  
            self.answers = []  
            self.qa_pairs = {}  
            for row in reader:  
                question_variants = row[0].strip().split(',')  
                answer_variants = row[1:]  
                self.questions.append(question_variants)  
                self.answers.append(answer_variants)  
                for q in question_variants:  
                    self.qa_pairs[q.strip()] = answer_variants  
        print("Questions and answers imported successfully from", filepath)  
    except FileNotFoundError:  
        print("Error: The specified file path is invalid.")  
    except PermissionError:  
        print("Error: Insufficient access privileges to read the file.")  
    except csv.Error:  
        print("Error: The CSV file is corrupted or has an unsupported format.")  
    except Exception as e:  
        print("An unexpected error occurred:", str(e))  
        self.save_error_logs_to_files(e)  

def save_error_logs_to_files(self, exception):  
    # Save traceback to a file  
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")  
    traceback_filename = f"traceback_{timestamp}.txt"  
    with open(traceback_filename, "w") as f:  
        traceback.print_exc(file=f)  
    print("Traceback saved to:", traceback_filename)  

    chatlog_filename = f"chatlog_{timestamp}.txt"  
    with open(chatlog_filename, "w") as f:  
        pass  
    print("Chat-log saved to:", chatlog_filename)  

def start_conversation(self):  
    if len(sys.argv) > 1 and sys.argv[1] == "--import" and sys.argv[2] == "--filetype" and sys.argv[3].lower() == "csv" and sys.argv[4] == "--filepath":  
        filepath = sys.argv[5]  
        self.import_from_csv(filepath)  
    elif len(sys.argv) > 1 and sys.argv[1] == "--question":  
        question = " ".join(sys.argv[2:])  
        self.handle_user_input(question)  
        sys.exit()  

    greeting = "Hello"  
    self.printwithtime(greeting)  
    while True:  
        self.printwithtime("How can I help you?")  
        userInput = input(self.getCurrentTimeString() + " ")  
        self.handle_user_input(userInput)  

def handle_user_input(self, userInput):  
    converted_to_lower_case = userInput.lower()  
    if len(converted_to_lower_case) == 1 or converted_to_lower_case in ["a", "an", "the"]:  
        self.printwithtime("Please provide a more specific query.")  
        return  
    if " and " in converted_to_lower_case or " hi, " in converted_to_lower_case or " or " in converted_to_lower_case:  
        compound_questions = re.split(r'\s+and\s+|\s+or\s+', converted_to_lower_case)  
        for question in compound_questions:  
            self.handle_single_question(question.strip())  
    else:  
        self.handle_single_question(converted_to_lower_case)  

def handle_single_question(self, question):  
    answers = []  
    if question in self.qa_pairs:  
        answers = self.qa_pairs[question]  
    elif question in ["hi", "hello", "hey"]:  
        answers.append("Hey!")  
    elif question == "bye":  
        answers.append("Goodbye! Have a great day!")  
        sys.exit()  
    else:  
        matched_questions = [q for q in self.qa_pairs.keys() if question in q.lower()]  
        if matched_questions:  
            self.printwithtime("Here are some related questions:")  
            for i, q in enumerate(matched_questions, 1):  
                print(f"{i}. {q}")  
            selected_question_index = input("Type the corresponding number to select a question: ")  
            if selected_question_index.isdigit() and int(selected_question_index) <= len(matched_questions):  
                selected_question = matched_questions[int(selected_question_index) - 1]  
                answers = self.qa_pairs[selected_question]  
            else:  
                answers.append("Invalid input. Please type the corresponding number.")  
        else:  
            self.printwithtime("Not recognized the question!! Please ask me again")  

    if answers:  
        random_answer = random.choice(answers)  
        self.printwithtime(random_answer)  # Print the random answer  

def getCurrentTimeString(self):  
    currenttime = datetime.datetime.now()  
    currenttimeString = currenttime.strftime("%X")  
    return currenttimeString  

def printwithtime(self, inputstring):  
    print(self.getCurrentTimeString() + " " + inputstring)  
class ChatbotUnitTest(unittest.TestCase):
def setUp(self):
self.chatbot = Chatbot()

def test_handle_single_question(self):  
    self.chatbot.handle_single_question("when does the holiday start?")  
    self.assertIn(self.chatbot.getCurrentTimeString(), sys.stdout.getvalue())  

def test_handle_user_input(self):  
    self.chatbot.handle_user_input("when does the holiday start?")  
    self.assertIn(self.chatbot.getCurrentTimeString(), sys.stdout.getvalue())  

def test_start_conversation(self):  
    sys.argv = ['chatbot.py', '--question', 'when does the holiday start?']  
    self.chatbot.start_conversation()  
    self.assertIn(self.chatbot.getCurrentTimeString(), sys.stdout.getvalue())  
if name == 'main':
if len(sys.argv) > 1 and sys.argv[1] == "--debug":
sys.argv.pop(1)
unittest.main(argv=sys.argv)
else:
Chatbot().start_conversation()
