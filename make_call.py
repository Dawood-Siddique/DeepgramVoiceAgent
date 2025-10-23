from call_customer import CallCustomer

def main():
    # Replace with the actual phone number to call
    to_number = "+923037307931" 
    to_number = "+923403779199" 

    caller = CallCustomer()
    call = caller.make_call(to_number)
    print(f"Call initiated with SID: {call.sid}")

if __name__ == "__main__":
    main()