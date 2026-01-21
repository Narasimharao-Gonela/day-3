
# grade_calculator.py
def get_valid_marks():
    """
    Get valid marks input from user with validation.
    Returns an integer between 0 and 100, or -1 if invalid.
    """
    try:
        # Prompt user for marks input
        marks = float(input("\nEnter marks (0-100): "))
        
        # Check if marks are within valid range
        if marks < 0 or marks > 100:
            print("❌ Error: Marks must be between 0 and 100!")
            return -1
        
        # Convert to integer and return
        return int(marks)
    
    except ValueError:
        # Handle non-numeric input
        print("❌ Error: Please enter a valid number!")
        return -1



def calculate_grade(marks):
    """
    Calculate grade based on marks and provide detailed feedback.
    Uses if-elif-else with logical operators and nested conditions.
    """
    
    # Validate input before processing
    if marks < 0:
        return None
    
    
    
    # Grade A: Excellent (90-100)
    if marks >= 90:
        grade = "A"
        category = "Excellent"
        performance = "Outstanding"
    
    # Grade B: Good (80-89)
    elif marks >= 80:
        grade = "B"
        category = "Good"
        
        # Nested condition: distinguish between B+ and B-
        if marks >= 85:
            category = "Good (B+)"
        else:
            category = "Good (B-)"
        
        performance = "Strong"
    
    # Grade C: Average (70-79)
    elif marks >= 70:
        grade = "C"
        category = "Average"
        
        # Nested condition: check pass/near-pass threshold
        if marks >= 75:
            category = "Average (C+)"
            performance = "Acceptable"
        else:
            category = "Average (C-)"
            performance = "Needs Improvement"
    
    # Grade D: Below Average (60-69)
    elif marks >= 60:
        grade = "D"
        category = "Below Average"
        
        # Nested condition: warning threshold
        if marks >= 65:
            performance = "Pass with Warning"
        else:
            performance = "Close to Failure"
    
    # Grade F: Fail (Below 60)
    else:
        grade = "F"
        category = "Fail"
        performance = "Failed - Retake Required"
    
    # Return dictionary with all information
    return {
        "marks": marks,
        "grade": grade,
        "category": category,
        "performance": performance
    }


# ======= FUNCTION TO DISPLAY RESULT WITH FEEDBACK =======
def display_result(result):
    """
    Display grade result with appropriate feedback and recommendations.
    Uses logical operators to determine recommendations.
    """
    
    if result is None:
        return
    
    marks = result["marks"]
    grade = result["grade"]
    category = result["category"]
    performance = result["performance"]
    
    # Display header
    print("\n" + "="*50)
    print("GRADE REPORT")
    print("="*50)
    
    # Display marks and grade
    print(f"📊 Marks Obtained: {marks}/100")
    print(f"📈 Grade: {grade}")
    print(f"📝 Category: {category}")
    print(f"🎯 Performance: {performance}")
    
    # ===== LOGICAL OPERATORS FOR RECOMMENDATIONS =====
    
    # Excellent performance recommendation
    if marks >= 90:
        print("\n✅ Congratulations! Excellent work!")
        print("   Keep up this outstanding performance!")
    
    # Good performance recommendation
    elif marks >= 80 and marks < 90:
        print("\n✅ Well done! You performed well.")
        print("   Continue maintaining this level of excellence.")
    
    # Average performance recommendation
    elif marks >= 70 and marks < 80:
        print("\n⚠️  You have passed, but there is room for improvement.")
        print("   Focus on understanding weak areas.")
    
    # Below average performance recommendation
    elif marks >= 60 and marks < 70:
        print("\n⚠️  You have barely passed. This is concerning.")
        print("   Seek immediate help and study harder.")
    
    # Fail recommendation
    else:
        print("\n❌ Unfortunately, you have failed.")
        print("   Please consult with your instructor and plan for retake.")
    
    # Additional feedback based on nested logic
    if marks >= 90:
        print("   🏆 You are eligible for scholarships or honors!")
    
    elif marks >= 75 and marks < 90:
        print("   📚 Good foundation - build upon this success!")
    
    elif marks >= 60 and marks < 75:
        print("   💪 Effort required - attend tutoring sessions!")
    
    else:
        print("   🆘 Critical support needed - contact academic advisor!")
    
    print("="*50)


# ======= FUNCTION TO CHECK ELIGIBILITY FOR DIFFERENT PROGRAMS =====
def check_eligibility(marks):
    """
    Check eligibility for different programs based on marks.
    Demonstrates complex nested conditions with logical operators.
    """
    
    print("\n" + "-"*50)
    print("PROGRAM ELIGIBILITY CHECK")
    print("-"*50)
    
    # Honors program eligibility (marks >= 90 AND consistent performance)
    if marks >= 90:
        print("✅ Eligible for: Honors Program")
        print("   Requirements: GPA >= 3.8, consistent excellence")
    
    # Advanced track eligibility (marks >= 80 AND mark >= 75)
    elif marks >= 80:
        print("✅ Eligible for: Advanced Track")
        print("   Requirements: Recommended for advanced courses")
    
    # Regular track eligibility (marks >= 70 AND mark >= 60)
    elif marks >= 70:
        print("✅ Eligible for: Regular Track")
        print("   Requirements: Standard curriculum")
    
    # Remedial support eligibility (marks < 60 OR marks < 70)
    elif marks >= 60:
        print("⚠️  Needs: Academic Support")
        print("   Requirements: Tutoring sessions mandatory")
    
    else:
        print("❌ Ineligible: Requires Remedial Classes")
        print("   Requirements: Basic foundation courses required")


# ======= MAIN PROGRAM =======
def main():
    """
    Main program to run the grade calculator.
    Demonstrates program flow and user interaction.
    """
    
    print("="*50)
    print("WELCOME TO GRADE CALCULATOR")
    print("="*50)
    
    # Flag to control loop
    continue_program = True
    
    while continue_program:
        # Get valid marks from user
        marks = get_valid_marks()
        
        # Process only if marks are valid
        if marks >= 0:  # Valid input
            # Calculate grade
            result = calculate_grade(marks)
            
            # Display result
            if result:
                display_result(result)
                
                # Check eligibility for programs
                check_eligibility(marks)
        
        # Ask if user wants to calculate another grade
        again = input("\n\nDo you want to calculate another grade? (yes/no): ").lower()
        
        if again not in ["yes", "y"]:
            continue_program = False
    
    print("\n" + "="*50)
    print("Thank you for using Grade Calculator!")
    print("="*50)


# ======= PROGRAM EXECUTION =======
if __name__ == "__main__":
    # Run the main program
    main()


# ======= TEST CASES (Uncomment to test without user input) =======
"""
# Test with multiple inputs
print("\\n\\nTEST CASES:")
test_marks = [95, 87, 76, 64, 55, 100, 0, 50]

for marks in test_marks:
    result = calculate_grade(marks)
    display_result(result)
    check_eligibility(marks)
"""
