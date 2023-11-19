import streamlit as st
import json

# JSON data with simple and complex questions
data = {
  "SimpleQuestions": [
    {
      "Question": "What is the best way to brush teeth?",
      "Answer": "Use a soft-bristled brush, brush twice a day for two minutes using fluoride toothpaste, and use circular motions at a 45-degree angle to the gums."
    },
    {
      "Question": "How often should I visit the dentist?",
      "Answer": "Generally, every six months for a routine check-up and cleaning, but this may vary based on individual dental health needs."
    },
    {
      "Question": "What are cavities?",
      "Answer": "Cavities are decayed areas of your teeth that develop into tiny openings or holes, often caused by a combination of factors including bacteria, snacking, sugary drinks, and poor teeth cleaning."
    },
    {
      "Question": "Why is flossing important?",
      "Answer": "Flossing removes plaque and food particles between teeth where a toothbrush can't reach, reducing the risk of cavities and gum disease."
    },
    {
      "Question": "What is gum disease?",
      "Answer": "Gum disease, or periodontal disease, is an infection of the tissues that hold your teeth in place, often due to poor brushing and flossing habits that allow plaque to build up on the teeth."
    },
    {
      "Question": "Can diet affect my oral health?",
      "Answer": "Yes, a diet high in sugar and carbohydrates can contribute to tooth decay, while a balanced diet is essential for good oral health."
    },
    {
      "Question": "What causes bad breath?",
      "Answer": "Bad breath can be caused by certain foods, poor dental hygiene, dry mouth, tobacco products, or medical conditions."
    },
    {
      "Question": "How can I prevent tooth decay?",
      "Answer": "Brush and floss regularly, reduce sugar intake, eat a balanced diet, and visit your dentist regularly for cleanings and checkups."
    },
    {
      "Question": "What is the best toothpaste to use?",
      "Answer": "A fluoride toothpaste approved by your local dental association is generally recommended for most people."
    },
    {
      "Question": "Is mouthwash necessary?",
      "Answer": "Mouthwash can be a helpful addition to good oral hygiene practices but is not a substitute for brushing and flossing."
    }
  ],
  "ComplexQuestions": [
    {
      "Question": "How does plaque affect teeth and gums?",
      "Answer": "Plaque is a sticky film of bacteria that forms on teeth. It produces acids that can lead to tooth decay and irritate gums, potentially causing gum disease. Over time, plaque can harden into tartar, which makes cleaning more difficult and exacerbates gum irritation."
    },
    {
      "Question": "What are the stages and treatment of periodontal disease?",
      "Answer": "Periodontal disease progresses through stages, starting with gingivitis, characterized by red, swollen gums that bleed easily. If untreated, it can advance to periodontitis, where gums pull away from teeth, forming pockets that can become infected. Advanced stages can lead to bone and tooth loss. Treatment varies from deep cleaning and medications to surgical interventions in severe cases."
    },
    {
      "Question": "What are the indications and procedures for root canal therapy?",
      "Answer": "Root canal therapy is indicated for a tooth with an infected or dead pulp, often due to severe decay or injury. The procedure involves removing the damaged pulp, cleaning and disinfecting the inner chamber of the tooth, and then filling and sealing it. A crown may be placed afterward for protection."
    },
    {
      "Question": "How do dental implants work, and who are they suitable for?",
      "Answer": "Dental implants are metal posts surgically positioned into the jawbone beneath the gums to replace the roots of missing teeth. Over time, they fuse to the jawbone providing stable support for artificial teeth. They are suitable for individuals with one or more missing teeth, adequate bone density, and good overall health."
    },
    {
      "Question": "What are the risks and benefits of orthodontic treatments like braces?",
      "Answer": "Orthodontic treatments correct misaligned teeth and jaws. Benefits include improved oral health, appearance, and function. Risks can include discomfort, difficulty in cleaning teeth during treatment, and, in rare cases, root resorption."
    },
    {
      "Question": "Can periodontal disease affect overall health?",
      "Answer": "Yes, periodontal disease has been linked to systemic health issues such as heart disease, diabetes, and stroke, likely due to inflammation and bacteria entering the bloodstream from the gums."
    },
    {
      "Question": "What are the latest advancements in dental technology?",
      "Answer": "Recent advancements include digital X-rays, which reduce radiation exposure; laser dentistry, used in various procedures for more precision; and CAD/CAM technology for same-day crowns and restorations."
    },
    {
      "Question": "What are the different types of dental fillings, and how are they chosen?",
      "Answer": "Common types include amalgam (silver), composite (tooth-colored), and gold. The choice depends on the tooth's location, the extent of decay, patient allergies, and aesthetic considerations."
    },
    {
      "Question": "How does age affect oral health?",
      "Answer": "Aging can increase the risk of dental issues like dry mouth, wear and tear on teeth, gum disease, and oral cancer. Medications and systemic health conditions common in older adults can also impact oral health."
    },
    {
      "Question": "What are the treatment options for TMJ disorders?",
      "Answer": "Treatment for temporomandibular joint (TMJ) disorders may include oral splints or mouth guards, physical therapy, medications, and in severe cases, surgical interventions. Treatment plans are often multidisciplinary, addressing both the physical and, sometimes, psychological aspects of the disorder."
    }
  ]
}

def main():
    st.title("🦷Dental Health Q&A")

    user_type = st.radio("Do you have a simple or complex question about you teeth?", ('Simple', 'Complex'))

    if user_type == 'Simple':
        questions = [q["Question"] for q in data["SimpleQuestions"]]
        question = st.selectbox("Select a question:", questions)
        for item in data["SimpleQuestions"]:
            if item["Question"] == question:
                st.write(item["Answer"])

    elif user_type == 'Complex':
        questions = [q["Question"] for q in data["ComplexQuestions"]]
        question = st.selectbox("Select a question:", questions)
        for item in data["ComplexQuestions"]:
            if item["Question"] == question:
                st.write(item["Answer"])


     # Button to talk to a dentist
    dentist_url = "https://portal.ada.org.au/Portal/Shared_Content/Smart-Suite/Smart-Maps/Public/Find-a-Dentist.aspx"
    if st.button("Talk to a Dentist!"):
        st.write('You are being directed to the Find A Dentist Portal!👩')
        js = f"window.open('{dentist_url}')"  # JavaScript to open a new window/tab
        st.components.v1.html(f"<script>{js}</script>", height=0)

if __name__ == "__main__":
    main()
