import requests

class GetPrograms:

    def get_programs(self):
        URL = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"
        response = requests.get(URL)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            return response.json()  # Use response.json() to directly parse JSON
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
            return None

    def program_agencies(self):
        programs_list = []
        programs = self.get_programs()

        if programs:  # Check if programs is not None
            for program in programs:
                programs_list.append(program.get("agency"))

        return programs_list

# Instantiate the class
programs_instance = GetPrograms()

# Call the method to get program agencies
agencies = programs_instance.program_agencies()

# Print the unique agency names
for agency in set(agencies):
    print(agency)
