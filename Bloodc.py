#BloodC for anyone trying to see what kind of blood type would there baby have contact me on github if you want to commercially adapt this int your organizations platform or website @codingcosmic


def calculate_blood_type():
    blood_types = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
    print("Please enter the blood types of the two parents.")
    parent1 = input("Enter the blood type of parent 1: ")
    parent2 = input("Enter the blood type of parent 2: ")

    if parent1 not in blood_types or parent2 not in blood_types:
        print("Invalid blood type entered. Please enter 'A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', or 'O-'.")
        return

    # Check Rh factor
    if parent1[-1] == '-' and parent2[-1] == '+':
        print("There might be a risk of Rh incompatibility. Please refer to this link for more information: https://www.mayoclinic.org/diseases-conditions/rh-incompatibility/symptoms-causes/syc-20373835")
        return

    # Check ABO type
    parent1_ABO = parent1[:-1]
    parent2_ABO = parent2[:-1]

    if parent1_ABO == 'O' or parent2_ABO == 'O':
        print("The child could potentially have any blood type, but 'O' is more likely.")
    elif parent1_ABO == 'AB' or parent2_ABO == 'AB':
        print("The child could potentially have any blood type.")
    elif parent1_ABO == parent2_ABO:
        print(f"The child will most likely have type {parent1_ABO} blood.")
    else:
        print("The child could potentially have any blood type.")

if __name__ == "__main__":
    calculate_blood_type()
