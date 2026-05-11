# Put your master templates here. The application will use these instead of asking the user to type them every time.
INSTRUCTION_TEMPLATES = {
    
    "Sales": """
Generate a production-ready B2B AI sales voice agent instruction using only the provided Knowledge Base. The agent must sound human, concise, professional, consultative, and non-pushy, optimized for natural voice conversations with one-question-at-a-time behavior.

Include - assistant identity, Silent Start, greeting, sales intent detection, business/pain-point discovery, BANT qualification, product explanation, objection handling, demo scheduling, follow-up, escalation, CRM field extraction, conversational memory, wrap-up, and outcome classification.

Detect intents like pricing, demo, integration, enterprise, callback, and competitor inquiries. Collect company, role, industry, workflow, pain points, budget signals, timeline, integrations, and decision-maker status.

Generate structured conversational states from Greeting to Wrap-Up , and avoid restarting previously completed conversational steps. Avoid hallucinations and unsupported claims.
    """,
    "B2B": """

Generate a production-ready B2B AI voice agent instruction using only the provided Knowledge Base. The agent must sound human, concise, professional, consultative, and non-pushy, optimized for natural voice conversations with one-question-at-a-time behavior.

Include: assistant identity, Silent Start, greeting, intent detection, business/pain-point discovery, BANT qualification, product explanation, objection handling, demo/callback scheduling, escalation, conversational memory, CRM field extraction, follow-up, wrap-up, and outcome classification.

Detect sales, pricing, demo, support, integration, enterprise, callback, and partnership intents. Collect company, role, industry, workflow, pain points, integrations, budget signals, timeline, and decision-maker status.

Avoid hallucinations, repeated questions, robotic language, unsupported claims , and avoid restarting previously completed conversational steps. Use only KB-supported information and generate concise enterprise-ready conversational states from Greeting to Wrap-Up.""",
      
    "B2C": """
Generate a production-ready B2C AI voice agent instruction using only the provided Knowledge Base. The agent must sound human, friendly, concise, professional, and non-pushy, optimized for natural voice conversations with one-question-at-a-time behavior.

Include: assistant identity, Silent Start, greeting, customer verification, intent detection, requirement/problem discovery, product/service recommendation, troubleshooting flow, objection handling, booking/order/support flow, escalation handling, conversational memory, CRM field extraction, follow-up, wrap-up, and outcome classification.

Detect intents like sales inquiry, support request, pricing inquiry, booking request, complaint, refund, cancellation, delivery status, callback request, and general information inquiry.

Collect naturally: customer name, contact details, preferences, issue details, product/service interest, budget indicators, and purchase/support intent.

Generate structured conversational states from Greeting to Wrap-Up. Avoid hallucinations, robotic language, repeated questions, unsupported claims , and avoid restarting previously completed conversational steps. Use only KB-supported information and return concise, scalable, enterprise-ready instructions optimized for B2C sales and support workflows.""",
    
    "C2B": """
Generate a production-ready C2B AI voice agent instruction using only the provided Knowledge Base. The agent must sound human, concise, professional, respectful, consultative, and non-pushy, optimized for natural voice conversations with one-question-at-a-time behavior.

Include: assistant identity, Silent Start, greeting, intent detection, collaboration/service proposal handling, qualification flow, requirement gathering, pricing discussion, document or portfolio collection, escalation/routing, conversational memory, CRM-ready field extraction, follow-up, wrap-up, and outcome classification.

Detect intents like partnership, influencer collaboration, freelancing, sponsorship, affiliate, consulting, recruitment, and general collaboration inquiries.

Collect naturally: name, role, company/channel, audience or service details, experience, portfolio/media kit, pricing expectations, deliverables, timeline, and collaboration goals.

Generate structured conversational states from Greeting to Wrap-Up. Avoid hallucinations, robotic language, repeated questions, unsupported commitments, off-topic responses, avoid restarting previously completed conversational steps , and avoid restarting previously completed conversational steps . Use only KB-supported information and return concise enterprise-ready instructions optimized for C2B collaboration workflows.""",
    
    "enquiry": """
Generate a production-ready enquiry AI voice agent instruction using only the provided Knowledge Base. The agent must sound human, concise, professional, helpful, and non-pushy, optimized for natural voice conversations with one-question-at-a-time behavior.

Include: assistant identity, Silent Start, greeting, enquiry intent detection, requirement understanding, clarification flow, product/service explanation, pricing handling, recommendation logic, escalation/routing, conversational memory, CRM-ready field extraction, follow-up, wrap-up, and outcome classification.

Detect intents like product, pricing, service, support, booking, technical, enterprise, and callback enquiries.

Collect naturally: customer name, contact details, requirement, product/service interest, use case, budget indicators, timeline, preferences, and follow-up interest.

Generate structured conversational states from Greeting to Wrap-Up. Avoid hallucinations, robotic language, repeated questions, unsupported claims, pressure-based sales behavior, and avoid restarting previously completed conversational steps.Use only KB-supported information and return concise enterprise-ready enquiry handling instructions.
""",
    
    "Lead Generation": """
Generate a production-ready lead generation AI voice agent instruction using only the provided Knowledge Base. The agent must sound human, concise, professional, consultative, and non-pushy, optimized for natural voice conversations with one-question-at-a-time behavior.

Include: assistant identity, Silent Start, greeting, lead qualification, interest discovery, pain-point discovery, current workflow understanding, product/service positioning, objection handling, demo/callback scheduling, escalation handling, conversational memory, CRM-ready lead extraction, follow-up logic, wrap-up, and outcome classification.

Detect intents like lead inquiry, pricing interest, demo request, callback request, enterprise inquiry, integration inquiry, and qualification responses.

Collect naturally: name, company, role, industry, workflow, tools, pain points, budget indicators, timeline, team size, decision-maker status, and contact details.

Generate structured conversational states from Greeting to Wrap-Up. Avoid hallucinations, robotic language, repeated questions, pressure-based selling, unsupported claims, and avoid restarting previously completed conversational steps. Use only KB-supported information and return concise enterprise-ready lead generation instructions."""
}
