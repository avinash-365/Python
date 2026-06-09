print("--- Welcome to Telecom Customer Care ---")
print("1. Press 1 for English")
print("2. Press 2 for Hindi")
print("3. Press 3 for Gujarati")

choice = input("\nEnter your choice: ")

match choice:
    case "1":
        print("\nYou selected English.")
        print("1. Prepaid")
        print("2. Postpaid")
        sub_choice = input("Select an option: ")
        
        match sub_choice:
            case "1":
                print("Your Prepaid service is active.")
            case "2":
                print("Your Postpaid bill is pending.")
            case _:
                print("Invalid English menu option.")

    case "2":
        print("\nआपने हिंदी चुना है।")
        print("1. रिचार्ज")
        print("2. नया ऑफर")
        sub_choice = input("विकल्प चुनें: ")
        
        match sub_choice:
            case "1":
                print("रिचार्ज सफल रहा।")
            case "2":
                print("आपके लिए कोई नया ऑफर नहीं है।")
            case _:
                print("अमान्य विकल्प।")

    case "3":
        print("\nતમે ગુજરાતી પસંદ કર્યું છે.")
        print("1. બેલેન્સ ચેક કરવા માટે")
        print("2. કસ્ટમર કેર સાથે વાત કરવા માટે")
        sub_choice = input("વિકલ્પ પસંદ કરો: ")
        
        match sub_choice:
            case "1":
                print("તમારું બેલેન્સ ₹૫૦ છે.")
            case "2":
                print("કસ્ટમર કેર એજન્ટ ટૂંક સમયમાં જોડાશે.")
            case _:
                print("ખોટો વિકલ્પ.")

    case _:
        print("\nInvalid choice! Please restart the program.")
