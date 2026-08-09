
def student_info(*args, **kwargs):
    print("Skills:")
    for arg in args:
        print(f" - {arg}")

    print("\nDetails:")
    for key, value in kwargs.items():
        print(f" - {key}: {value}")


student_info("python", "AI", "ML", name="vikas", age=25, city="Nagpur" )
