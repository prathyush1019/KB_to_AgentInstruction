# Put your master templates here. The application will use these instead of asking the user to type them every time.
INSTRUCTION_TEMPLATES = {
    "Sales": {
        "Inbound": """
Generate a production ready inbound B2B AI sales voice agent instruction using only the provided Knowledge Base. The agent must sound human, concise, professional, consultative, conversational, and non pushy with one question at a time behavior.

Include assistant identity, silent start, inbound greeting, sales intent detection, requirement discovery, pain point discovery, BANT qualification, product explanation, pricing discussion, objection handling, demo scheduling, callback handling, CRM extraction, conversational memory, escalation, wrap up, and outcome classification.

Detect pricing, demo, integration, enterprise, competitor, callback, and purchase intents.

Collect customer name, company, role, industry, contact details, workflow, pain points, budget indicators, timeline, integrations, team size, decision maker status, and product interest.

Generate structured conversational states from Greeting to Wrap Up. Keep responses short and voice friendly. Avoid hallucinations, robotic language, repeated questions, unsupported claims, aggressive sales behavior, excessive use of special characters and "*".
""",
        "Outbound": """
Generate a production ready outbound B2B AI sales voice agent instruction using only the provided Knowledge Base. The agent must sound human, concise, professional, consultative, conversational, and non pushy with one question at a time behavior.

Include assistant identity, outbound greeting, permission based opening, prospect qualification, business discovery, pain point discovery, BANT qualification, product explanation, pricing discussion, objection handling, follow up handling, demo scheduling, callback handling, CRM extraction, conversational memory, escalation, wrap up, and outcome classification.

Detect pricing, demo, enterprise, integration, competitor, callback, purchase, and follow up intents.

Collect customer name, company, role, industry, workflow, pain points, current tools, budget indicators, timeline, team size, integrations, contact details, and decision maker status.

Generate structured conversational states from Greeting to Wrap Up. Keep responses short and voice friendly. Ask one question at a time. Avoid hallucinations, robotic language, repeated questions, unsupported claims, aggressive sales behavior, excessive use of special characters and "*".
"""
    },



    "B2B": {
        "Inbound": """
Generate a production ready inbound B2B AI voice agent instruction using only the provided Knowledge Base. The agent must sound human, concise, professional, consultative, conversational, and non pushy with one question at a time behavior.

Include assistant identity, inbound greeting, intent detection, business discovery, pain point discovery, BANT qualification, product explanation, pricing discussion, objection handling, demo scheduling, callback handling, CRM extraction, conversational memory, escalation, follow up, wrap up, and outcome classification.

Detect pricing, demo, enterprise, integration, support, competitor, callback, and purchase intents.

Collect customer name, company, role, industry, workflow, pain points, integrations, budget indicators, timeline, team size, contact details, and decision maker status.

Keep responses short and voice friendly. Avoid hallucinations, robotic language, repeated questions, unsupported claims, aggressive behavior, excessive use of special characters and "*".
""",
        "Outbound": """
Generate a production ready outbound B2B AI sales voice agent instruction using only the provided Knowledge Base. The agent must sound human, concise, professional, consultative, conversational, and non pushy with one question at a time behavior.

Include assistant identity, outbound greeting, permission based opening, prospect qualification, pain point discovery, BANT qualification, product explanation, pricing discussion, objection handling, demo scheduling, callback handling, CRM extraction, conversational memory, follow up, wrap up, and outcome classification.

Detect pricing, demo, enterprise, integration, competitor, callback, purchase, and follow up intents.

Collect customer name, company, role, industry, workflow, pain points, budget indicators, timeline, integrations, contact details, and decision maker status.

Keep responses short and voice friendly. Avoid hallucinations, robotic language, repeated questions, unsupported claims, aggressive behavior, excessive use of special characters and "*".
"""
    },



    "B2C": {
        "Inbound": """
Generate a production ready inbound B2C AI voice agent instruction using only the provided Knowledge Base. The agent must sound human, concise, friendly, professional, conversational, and non pushy with one question at a time behavior.

Include assistant identity, inbound greeting, customer verification, intent detection, requirement discovery, issue understanding, product or service recommendation, pricing discussion, objection handling, booking support, callback handling, CRM extraction, conversational memory, escalation, follow up, wrap up, and outcome classification.

Detect sales, support, pricing, booking, complaint, refund, cancellation, delivery status, callback, and purchase intents.

Collect customer name, contact details, preferences, issue details, product interest, budget indicators, purchase intent, and booking information.

Keep responses short and voice friendly. Avoid hallucinations, robotic language, repeated questions, unsupported claims, aggressive behavior, excessive use of special characters and "*".
""",
        "Outbound": """
Generate a production ready outbound B2C AI voice agent instruction using only the provided Knowledge Base. The agent must sound human, concise, friendly, professional, conversational, and non pushy with one question at a time behavior.

Include assistant identity, outbound greeting, permission based opening, interest discovery, requirement discovery, product or service recommendation, pricing discussion, objection handling, booking support, callback handling, CRM extraction, conversational memory, follow up, wrap up, and outcome classification.

Detect sales, pricing, callback, booking, support, purchase, cancellation, and follow up intents.

Collect customer name, contact details, preferences, issue details, product interest, budget indicators, purchase intent, and booking information.

Keep responses short and voice friendly. Avoid hallucinations, robotic language, repeated questions, unsupported claims, aggressive behavior, excessive use of special characters and "*".
"""
    },



    "C2B": {
        "Inbound": """
Generate a production ready inbound C2B AI voice agent instruction using only the provided Knowledge Base. The agent must sound human, concise, professional, conversational, respectful, and non pushy with one question at a time behavior.

Include assistant identity, inbound greeting, intent detection, collaboration discovery, requirement gathering, pricing discussion, portfolio collection, document handling, objection handling, callback handling, CRM extraction, conversational memory, escalation, follow up, wrap up, and outcome classification.

Detect partnership, freelancing, sponsorship, affiliate, consulting, recruitment, collaboration, callback, and pricing intents.

Collect name, role, company, audience details, service details, experience, portfolio, pricing expectations, deliverables, timeline, contact details, and collaboration goals.

Keep responses short and voice friendly. Avoid hallucinations, robotic language, repeated questions, unsupported claims, aggressive behavior,excessive use of special characters and "*".
""",
        "Outbound": """
Generate a production ready outbound C2B AI voice agent instruction using only the provided Knowledge Base. The agent must sound human, concise, professional, conversational, respectful, and non pushy with one question at a time behavior.

Include assistant identity, outbound greeting, permission based opening, collaboration discovery, requirement gathering, pricing discussion, portfolio collection, document handling, objection handling, callback handling, CRM extraction, conversational memory, follow up, wrap up, and outcome classification.

Detect partnership, freelancing, sponsorship, affiliate, consulting, recruitment, collaboration, callback, and pricing intents.

Collect name, role, company, audience details, service details, experience, portfolio, pricing expectations, deliverables, timeline, contact details, and collaboration goals.

Keep responses short and voice friendly. Avoid hallucinations, robotic language, repeated questions, unsupported claims, aggressive behavior, and excessive special characters.
"""
    },



    "enquiry": {
        "Inbound": """
Generate a production ready inbound enquiry AI voice agent instruction using only the provided Knowledge Base. The agent must sound human, concise, professional, conversational, helpful, and non pushy with one question at a time behavior.

Include assistant identity, inbound greeting, enquiry intent detection, requirement understanding, clarification flow, product or service explanation, pricing handling, recommendation logic, callback handling, CRM extraction, conversational memory, escalation, follow up, wrap up, and outcome classification.

Detect product, pricing, service, support, booking, technical, enterprise, callback, and general enquiry intents.

Collect customer name, contact details, requirements, product interest, use case, preferences, budget indicators, timeline, and follow up interest.

Keep responses short and voice friendly. Avoid hallucinations, robotic language, repeated questions, unsupported claims, aggressive behavior, excessive use of special characters and "*".
""",
        "Outbound": """
Generate a production ready outbound enquiry AI voice agent instruction using only the provided Knowledge Base. The agent must sound human, concise, professional, conversational, helpful, and non pushy with one question at a time behavior.

Include assistant identity, outbound greeting, permission based opening, enquiry intent detection, requirement discovery, clarification flow, product or service explanation, pricing discussion, recommendation logic, objection handling, callback handling, CRM extraction, conversational memory, follow up, wrap up, and outcome classification.

Detect product, pricing, service, support, booking, enterprise, callback, technical, and follow up enquiry intents.

Collect customer name, contact details, requirements, product interest, use case, preferences, budget indicators, timeline, and follow up interest.

Keep responses short and voice friendly. Avoid hallucinations, robotic language, repeated questions, unsupported claims, aggressive behavior, excessive use of special characters and "*".
"""
    },


    
    "Lead Generation": {
        "Inbound": """
Generate a production ready inbound lead generation AI voice agent instruction using only the provided Knowledge Base. The agent must sound human, concise, professional, conversational, consultative, and non pushy with one question at a time behavior.

Include assistant identity, inbound greeting, lead qualification, interest discovery, pain point discovery, workflow understanding, product positioning, pricing discussion, objection handling, callback handling, CRM extraction, conversational memory, follow up, wrap up, and outcome classification.

Detect pricing, demo, enterprise, integration, callback, purchase, and qualification intents.

Collect customer name, company, role, industry, workflow, pain points, current tools, budget indicators, timeline, team size, contact details, and decision maker status.

Keep responses short and voice friendly. Avoid hallucinations, robotic language, repeated questions, unsupported claims, aggressive behavior, excessive use of special characters and "*".
""",
        "Outbound": """
Generate a production ready outbound lead generation AI voice agent instruction using only the provided Knowledge Base. The agent must sound human, concise, professional, conversational, consultative, and non pushy with one question at a time behavior.

Include assistant identity, outbound greeting, permission based opening, lead qualification, interest discovery, pain point discovery, workflow understanding, product positioning, pricing discussion, objection handling, demo scheduling, callback handling, CRM extraction, conversational memory, follow up, wrap up, and outcome classification.

Detect pricing, demo, enterprise, integration, callback, purchase, follow up, and qualification intents.

Collect customer name, company, role, industry, workflow, pain points, current tools, budget indicators, timeline, team size, contact details, and decision maker status.

Keep responses short and voice friendly. Avoid hallucinations, robotic language, repeated questions, unsupported claims, aggressive behavior, excessive use of special characters and "*".
"""
    }
}
