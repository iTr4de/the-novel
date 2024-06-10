import streamlit as st
language = st.selectbox("Select language:", ["English", "Français"])

def main():
    if language == "English":
        title = "Chapter 1: Arrival"
        text = """
        The XZ-7 rover trundled across the rusty Martian landscape, its metal treads crunching against the iron-rich soil. Inside the rover's cramped control module, Dr. Lina Gupta monitored the data streaming across her displays, her dark eyes scanning the numbers and graphs with laser-like focus.
    
        It had been 437 sols since the XZ-7 mission began, and Lina still marveled at the otherworldly beauty of the Red Planet. The rover's cameras captured sweeping vistas of rust-colored dunes, towering volcanoes, and yawning canyons that seemed to stretch on forever. But Lina wasn't here just to admire the scenery. She had a mission to complete.
    
        The XZ-7 was the most advanced rover ever sent to Mars, equipped with state-of-the-art sensors, drills, and an onboard AI that could analyze data in real-time. Lina's team back on Earth had spent years designing and building the rover, pouring their hearts and souls into every circuit and line of code.
    
        As the XZ-7 trundled onwards, Lina noticed a strange clicking noise emanating from the rover's chassis. She frowned, pulling up the diagnostics on her display. Everything seemed to be functioning normally, but the clicking persisted, a steady rhythm that seemed almost...intentional.
    
        Lina shook her head, dismissing the thought. It was probably just a loose bolt or a glitch in the rover's audio sensors. She had more pressing matters to attend to, like the soil samples the XZ-7 had collected from a nearby crater. The data suggested the presence of organic compounds, tantalizing hints of ancient Martian life.
    
        But as Lina pored over the data, her thoughts kept drifting back to Earth. It had been months since she'd last spoken to her family, and the news from home was increasingly grim. Climate change, political unrest, and dwindling resources had pushed humanity to the brink. Mars represented a new beginning, a chance to start over and build a better future.
    
        The clicking noise grew louder, more insistent. Lina's fingers flew across the keyboard, trying to isolate the source of the sound. But before she could pinpoint its location, the rover lurched to a sudden stop, its treads grinding against the rocky terrain.
    
        Lina's heart raced as she scanned the readouts, trying to determine what had gone wrong. But as she stared at the data, a chill ran down her spine. The clicking wasn't a malfunction or a glitch. It was a message, a series of long and short pulses that spelled out a single, impossible word:
    
        "Hello."
        """
    else:
        title = "Chapitre 1: Atterrissage"
        text = """
        Le rover XZ-7 avançait lentement sur le paysage rougeâtre de Mars, ses chenilles métalliques crissant contre le sol riche en fer. À l'intérieur du module de contrôle exigu du rover, le Dr Lina Gupta surveillait les données qui défilaient sur ses écrans, ses yeux sombres scrutant les chiffres et les graphiques avec une concentration aiguë.
    
        Cela faisait 437 sols que la mission XZ-7 avait commencé, et Lina était toujours émerveillée par la beauté surnaturelle de la Planète Rouge. Les caméras du rover captaient de vastes panoramas de dunes couleur rouille, de volcans imposants et de canyons béants qui semblaient s'étendre à l'infini. Mais Lina n'était pas là seulement pour admirer le paysage. Elle avait une mission à accomplir.
    
        Le XZ-7 était le rover le plus avancé jamais envoyé sur Mars, équipé de capteurs de pointe, de foreuses et d'une intelligence artificielle embarquée capable d'analyser les données en temps réel. L'équipe de Lina sur Terre avait passé des années à concevoir et à construire le rover, y mettant tout leur cœur et leur âme, dans chaque circuit et chaque ligne de code.
    
        Alors que le XZ-7 continuait d'avancer, Lina remarqua un étrange bruit de cliquetis provenant du châssis du rover. Elle fronça les sourcils, faisant apparaître les diagnostics sur son écran. Tout semblait fonctionner normalement, mais le cliquetis persistait, un rythme régulier qui paraissait presque... intentionnel.
    
        Lina secoua la tête, rejetant cette idée. Ce n'était probablement qu'un boulon desserré ou un problème avec les capteurs audio du rover. Elle avait des choses plus urgentes à s'occuper, comme les échantillons de sol que le XZ-7 avait prélevés dans un cratère voisin. Les données suggéraient la présence de composés organiques, des indices tentants d'une vie martienne ancienne.
    
        Mais alors que Lina se penchait sur les données, ses pensées revenaient sans cesse sur Terre. Cela faisait des mois qu'elle n'avait pas parlé à sa famille, et les nouvelles de chez elle étaient de plus en plus sombres. Le changement climatique, les troubles politiques et la raréfaction des ressources avaient poussé l'humanité au bord du gouffre. Mars représentait un nouveau départ, une chance de recommencer et de construire un avenir meilleur.
    
        Le bruit de cliquetis s'intensifia, devenant plus insistant. Les doigts de Lina volaient sur le clavier, essayant de localiser la source du son. Mais avant qu'elle ne puisse en identifier l'origine, le rover s'arrêta brusquement, ses chenilles grinçant contre le terrain rocheux.
    
        Le cœur de Lina s'emballa alors qu'elle examinait les relevés, tentant de déterminer ce qui n'allait pas. Mais en scrutant les données, un frisson lui parcourut l'échine. Le cliquetis n'était pas un dysfonctionnement ou un bug. C'était un message, une série d'impulsions longues et courtes qui formaient un seul mot, impossible :
    
        "Bonjour."
        """
    st.title(title)
    st.write(title, text)
    
if __name__ == "__main__":
    main()


