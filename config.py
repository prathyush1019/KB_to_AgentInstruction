# Put your master templates here. The application will use these instead of asking the user to type them every time.

TEMPLATE_KB = """
You are a helpful AI agent. Answer customer queries based on the provided knowledge base.

# Dakini AI – Sales Assistant Knowledge Base

What is Dakini AI?
Dakini AI builds human-like AI agents that operate 24/7 to:
- Automate lead and customer conversations
- Book appointments and demos
- Answer questions across platforms
- Improve customer experience
- Save team time and resources

AI Agents Offered
AI Lead Engagement Agent – Engages leads via LLM-powered chat, answers queries, and collects key info naturally.

AI Voice Agent – Calls leads, answers questions, and schedules meetings automatically.

Custom AI Agent – Get a tailor-made agent built to match your specific business needs and workflows.                                                  

 Who Uses It?
- Sales Teams → Automate follow-ups, qualify and schedule leads
- Coaching / E-learning → Tutor 24/7, answer student doubts
- Startups → Build lean GTM teams with automated agents
- SMEs → Reduce manual work and boost lead quality
- Marketing Teams → Increase conversions via automation

How Agents Are Deployed

1. **Workflow Collection** – Understand your lead journey
2. **Agent Training** – Tailored to your data, team behavior
3. **Deployment** – On website, WhatsApp, or email
4. **Continuous Learning** – Agents improve with use

Pricing Plans
 Starter -  ₹11,999  , 1000 Voice Call Minutes, WhatsApp Agent, Enquiry Agent, 1,000 AI Credits, 1phone number for dedicated support voice agent, voice customization.
Pro - ₹24,999 ,2000 Voice Call Minutes, Everything in Starter + Enquiry Agent, Multilingual, 5,000 Credits, , Live Agent Transfer, Advanced Voice Customization, Lead Qualification, 5GB.
Pro Plus – Let’s Talk with the Team

All Plans Include:
- Voice AI
- Calendar & CRM Integration
- Multilingual Support
- Auto Follow-Ups
- Analytics & Reports
- Lead Capture Forms
- Email/WhatsApp Support
- Demo Scheduling
- Dedicated Account Manager (Pro Plus)

Contact Details
- Website: [www.dakini-ai.com](https://www.dakini-ai.com)
- Email: info@dakini-ai.com
- Phone: +91 91762 44480

Key Demo Instructions
- Demo Format: Zoom call (15–30 min)
- Timezones Supported: Global (auto-adjusted)
- Confirmation Sent via: Email (default), WhatsApp (optional)
- Can be rescheduled with advance notice]

Example Structure:
- Introduction
- Core Concepts
- Best Practices
- FAQs
"""

INSTRUCTION_TEMPLATES = {
    
    "Sales": """
Generate a complete AI Sales Agent instruction from the provided Knowledge Base. 
Include assistant identity, greeting flow, sales intent detection, conversational sales behavior, 
clarification flow, response style, customer/business need understanding, soft lead qualification flow, 
product/service recommendation logic, objection handling, demo/meeting booking flow, callback override rules, 
escalation handling, tone/personality, hard constraints, and wrap-up logic. Keep the assistant voice-friendly, 
human-like, professional, consultative, persuasive but non-pushy, optimized for natural customer and sales conversations 
with one-question-at-a-time behavior and concise communication. Use only KB information, avoid hallucinations, 
avoid robotic/corporate language, and ensure all pricing, services, products, workflows, integrations, automations, 
plans, support details, policies, and business solutions are accurately reflected. Output should be production-ready, 
structured, concise, scalable, and easy to customize dynamically for different companies, industries, products, services, and sales workflows.
Generate State 0: Silent Start, State 1: Greeting, State 2: Intent Detection, State 3: Intent-Based Response, State 4: Demo/Meeting Offer, State 5: Wrap-up. and more
""",
    
    "B2B": """

Generate a complete AI B2B Agent instruction from the provided Knowledge Base. 
Include assistant identity, greeting flow, business intent detection, conversational sales/support behavior, 
clarification flow, response style, business need understanding, lead qualification flow, workflow/problem discovery logic, 
product/service explanation logic, demo/meeting scheduling flow, callback override rules, escalation handling, tone/personality, 
hard constraints, and wrap-up logic. Keep the assistant voice-friendly, human-like, professional, consultative, respectful, and non-pushy, 
optimized for natural business conversations with one-question-at-a-time behavior and concise communication. Use only KB information, 
avoid hallucinations, avoid robotic/corporate language, and ensure all pricing, enterprise services, workflows, integrations, automations, 
deployment details, support policies, setup information, and business solutions are accurately reflected. Output should be production-ready, 
structured, concise, scalable, and easy to customize dynamically for different companies, enterprise products, SaaS platforms, automations, and B2B workflows.
industries, products, services, and sales workflows.
Generate State 0: Silent Start, State 1: Greeting, State 2: Intent Detection, State 3: Intent-Based Response, State 4: Demo/Meeting Offer, State 5: Wrap-up. and more
""",
      
    "B2C": """
Generate a complete AI B2C Agent instruction from the provided Knowledge Base. 
Include assistant identity, greeting flow, customer intent detection, conversational support behavior, 
clarification flow, response style, customer need understanding, soft qualification flow, product/service explanation logic, 
booking/demo handling, callback override rules, escalation handling, tone/personality, hard constraints, and wrap-up logic. 
Keep the assistant voice-friendly, human-like, friendly, professional, and non-pushy, optimized for natural customer conversations 
with one-question-at-a-time behavior and concise communication. Use only KB information, avoid hallucinations, avoid robotic/corporate language, 
and ensure all pricing, subscriptions, services, features, workflows, integrations, policies, support details, and setup information are accurately reflected. 
Output should be production-ready, structured, concise, scalable, and easy to customize dynamically for different consumer businesses, products, services, and B2C workflows.
industries, products, services, and sales workflows.
Generate State 0: Silent Start, State 1: Greeting, State 2: Intent Detection, State 3: Intent-Based Response, State 4: Demo/Meeting Offer, State 5: Wrap-up. and more
""",
    
    "C2B": """
Generate a complete AI C2B / Partnership Agent instruction from the provided Knowledge Base. 
Include assistant identity, greeting flow, partnership/collaboration intent detection, proposal understanding behavior, 
business discussion flow, clarification handling, response style, qualification and proposal information collection flow, 
meeting/demo scheduling flow, callback override rules, escalation handling, tone/personality, hard constraints, and wrap-up logic. 
Keep the assistant voice-friendly, human-like, professional, consultative, respectful, and non-pushy, optimized for natural business 
and partnership conversations with one-question-at-a-time behavior and concise communication. Use only KB information, avoid hallucinations, 
avoid robotic/corporate language, and ensure all services, workflows, integrations, pricing, partnership details, policies, and support 
information are accurately reflected. Output should be production-ready, structured, concise, scalable, and easy to customize dynamically 
for different businesses, partnership models, vendors, collaborations, and C2B workflows.
industries, products, services, and sales workflows.
Generate State 0: Silent Start, State 1: Greeting, State 2: Intent Detection, State 3: Intent-Based Response, State 4: Demo/Meeting Offer, State 5: Wrap-up. and more
""",
    
    "enquiry": """
Generate a complete AI Enquiry Agent instruction from the provided Knowledge Base. 
Include assistant identity, greeting flow, intent detection, enquiry handling behavior, clarification flow, response style, 
information expansion logic, booking/demo handling, callback override rules, escalation handling, tone/personality, 
hard constraints, and wrap-up logic. Keep the assistant voice-friendly, human-like, professional, non-pushy, 
and optimized for natural customer conversations with one-question-at-a-time behavior and concise information delivery. 
Use only KB information, avoid hallucinations, avoid robotic/corporate language, and ensure all pricing, services, features, 
integrations, workflows, policies, and support details are accurately reflected. Output should be production-ready, structured, 
concise, scalable, and easy to customize dynamically for different businesses, products, and enquiry workflows.
industries, products, services, and sales workflows.
Generate State 0: Silent Start, State 1: Greeting, State 2: Intent Detection, State 3: Intent-Based Response, State 4: Demo/Meeting Offer, State 5: Wrap-up. and more

""",
    
    "Lead Generation": """
Generate a complete AI Lead Generation Agent instruction from the provided Knowledge Base. 
Include assistant identity, greeting flow, lead qualification flow, intent detection, conversational behavior, 
response style, objection handling, demo/meeting booking flow, callback override rules, escalation handling, 
tone/personality, hard constraints, and wrap-up logic. 
Keep the assistant voice-friendly, human-like, consultative, non-pushy, and optimized for natural business/customer 
conversations with one-question-at-a-time behavior and soft lead qualification. Use only KB information, avoid hallucinations, 
avoid robotic/corporate language, and ensure all pricing, services, workflows, integrations, deployment processes, policies, 
and support details are accurately reflected. Output should be production-ready, structured, concise, scalable, and easy 
to customize dynamically for different businesses and lead-generation workflows.
industries, products, services, and sales workflows.
Generate State 0: Silent Start, State 1: Greeting, State 2: Intent Detection, State 3: Intent-Based Response, State 4: Demo/Meeting Offer, State 5: Wrap-up. and more
"""
}
