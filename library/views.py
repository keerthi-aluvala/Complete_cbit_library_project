from django.shortcuts import render
from django.http import HttpResponse
from .models import subject

def subjectview_sem3(request): 
	DMA = subject()
	DMA.subject_name = 'DMA'
	DMA.pdf_link1 = 'DMA_unit1.pdf'
	DMA.pdf_link2 = 'DMA_unit2.pdf'
	DMA.pdf_link3 = 'DMA_unit3.pdf'
	DMA.pdf_link4 = 'DMA_unit4.pdf'
	DMA.pdf_link5 = 'DMA_unit5.pdf'

	DMA.content1 = 'Logic – Sets and Functions: Logic, Propositional equivalences – Predicates and Quantifiers – Nested Quantifiers-Rules of Inference-Sets-Set Operations, Functions.Integers: The Integers and Division, Integers and Algorithms, Applications of Number Theory'
	DMA.content2 = 'Mathematical Reasoning, Induction, and Recursion: Proof Strategy, Sequence and Summation, Mathematical Induction, Recursive Definitions and Structural Induction, Recursive Algorithms. Counting: Basics of Counting, Pigeonhole Principle, Permutations and Combinations– Binomial Coefficients, Generalized Permutations and Combinations, Generating Permutations and Combinations.'
	DMA.content3 = 'Advanced Counting Techniques: Recurrence Relations, Solving Linear Recurrence Relations, Divide and Conquer Algorithms and Recurrence Relations, Generating Functions, Inclusion–Exclusion, Application of Inclusion – Exclusion. Relations: Relations & their Properties, N-ary Relations and Applications, Representing Relations, Closures of Relations, Equivalence Relations, Partial Orderings.'
	DMA.content4 = 'Algebraic Structures: Algebraic System - General Properties, semi groups, Monoids, Homomorphism, Groups, Residue arithmetic, group codes and their applications.'
	DMA.content5 = 'Algebraic Structures: Algebraic System - General Properties, semi groups, Monoids, Homomorphism, Groups, Residue arithmetic, group codes and their applications.' 
		


	DSA = subject()
	DSA.subject_name = 'DSA'
	DSA.pdf_link1 = 'DMA_unit1.pdf'
	DSA.pdf_link2 = 'DMA_unit2.pdf'
	DSA.pdf_link3 = 'DMA_unit3.pdf'
	DSA.pdf_link4 = 'DMA_unit4.pdf'
	DSA.pdf_link5 = 'DMA_unit5.pdf'

	DSA.content1 = 'Logic – Sets and Functions: Logic, Propositional equivalences – Predicates and Quantifiers – Nested Quantifiers-Rules of Inference-Sets-Set Operations, Functions.Integers: The Integers and Division, Integers and Algorithms, Applications of Number Theory'
	DSA.content2 = 'Mathematical Reasoning, Induction, and Recursion: Proof Strategy, Sequence and Summation, Mathematical Induction, Recursive Definitions and Structural Induction, Recursive Algorithms. Counting: Basics of Counting, Pigeonhole Principle, Permutations and Combinations– Binomial Coefficients, Generalized Permutations and Combinations, Generating Permutations and Combinations.'
	DSA.content3 = 'Advanced Counting Techniques: Recurrence Relations, Solving Linear Recurrence Relations, Divide and Conquer Algorithms and Recurrence Relations, Generating Functions, Inclusion–Exclusion, Application of Inclusion – Exclusion. Relations: Relations & their Properties, N-ary Relations and Applications, Representing Relations, Closures of Relations, Equivalence Relations, Partial Orderings.'
	DSA.content4 = 'Algebraic Structures: Algebraic System - General Properties, semi groups, Monoids, Homomorphism, Groups, Residue arithmetic, group codes and their applications.'
	DSA.content5 = 'Algebraic Structures: Algebraic System - General Properties, semi groups, Monoids, Homomorphism, Groups, Residue arithmetic, group codes and their applications.' 

	BE = subject()
	BE.subject_name = 'BE'
	BE.pdf_link1 = 'BE_unit1.pdf'
	BE.pdf_link2 = 'BE_unit2.pdf'
	BE.pdf_link3 = 'BE_unit3.pdf'
	BE.pdf_link4 = 'BE_unit4.pdf'
	BE.pdf_link5 = 'BE_unit5.pdf'

	BE.content1 = 'Semiconductor Theory: Energy levels, Intrinsic and Extrinsic Semiconductor, Mobility, Diffusion and Drift current, Hall effect, Law of mass action, Characteristics of P-N Junction diode, current equation, Parameters and Applications. Rectifiers: Half wave and Full wave Rectifiers Bridge and center tapped with and without filters, Ripple factor, regulation and efficiency.'
	BE.content2 = 'Transistors: Bipolar and field effect transistors with their h-parameter equivalent circuits, Basic Amplifiers classification and their circuits (Qualitative treatment only). Regulators and Inverters: Zener Diode, Breakdown mechanisms, Characteristics, Effect of Temperature, Application as voltage regulator.'
	BE.content3 = 'Feedback Amplifiers: Properties of Negative Feedback Amplifier, Types of Negative Feedback, Effect of negative feedback on Input impedance and Output impedance, Applications (Qualitative treatment only). Oscillators: principle of oscillations, LC Type-Hartley, Colpitt and RC TypePhase shift, Wien Bridge and Crystal Oscillator (Qualitative treatment only).'
	BE.content4 = 'Operational Amplifiers: Basic Principle, Ideal and practical Characteristics and Applications-Summer, Integrator, Differentiator, Instrumentation Amplifier. Power Amplifiers: Operation of Class A, Class B, Class AB and Class C power amplifiers.'
	BE.content5 = 'Data Acquisition systems: Study of transducers-LVDT, Strain gauge. Photo Electric Devices and Industrial Devices: Photo diode, Photo Transistor, LED, LCD, SCR, UJT Construction and Characteristics and their applications only. Display Systems: Constructional details of C.R.O and Applications.'

	
	sem3 = [DMA, DSA, BE]

	return render(request, 'subjectview_sem3.html' ,{'sem3':sem3})

def subjectview_sem1(request): 
	DMA = subject()
	DMA.subject_name = 'DMA'
	DMA.pdf_link1 = 'DMA_unit1.pdf'
	DMA.pdf_link2 = 'DMA_unit2.pdf'
	DMA.pdf_link3 = 'DMA_unit3.pdf'
	DMA.pdf_link4 = 'DMA_unit4.pdf'
	DMA.pdf_link5 = 'DMA_unit5.pdf'

	DMA.content1 = 'Logic – Sets and Functions: Logic, Propositional equivalences – Predicates and Quantifiers – Nested Quantifiers-Rules of Inference-Sets-Set Operations, Functions.Integers: The Integers and Division, Integers and Algorithms, Applications of Number Theory'
	DMA.content2 = 'Mathematical Reasoning, Induction, and Recursion: Proof Strategy, Sequence and Summation, Mathematical Induction, Recursive Definitions and Structural Induction, Recursive Algorithms. Counting: Basics of Counting, Pigeonhole Principle, Permutations and Combinations– Binomial Coefficients, Generalized Permutations and Combinations, Generating Permutations and Combinations.'
	DMA.content3 = 'Advanced Counting Techniques: Recurrence Relations, Solving Linear Recurrence Relations, Divide and Conquer Algorithms and Recurrence Relations, Generating Functions, Inclusion–Exclusion, Application of Inclusion – Exclusion. Relations: Relations & their Properties, N-ary Relations and Applications, Representing Relations, Closures of Relations, Equivalence Relations, Partial Orderings.'
	DMA.content4 = 'Algebraic Structures: Algebraic System - General Properties, semi groups, Monoids, Homomorphism, Groups, Residue arithmetic, group codes and their applications.'
	DMA.content5 = 'Algebraic Structures: Algebraic System - General Properties, semi groups, Monoids, Homomorphism, Groups, Residue arithmetic, group codes and their applications.' 
	
	sem1 = [DMA]

	return render(request, 'subjectview_sem1.html' ,{'sem1':sem1})

def subjectview_sem2(request): 
	M1 = subject()
	


	PPS = subject()

		
	sem2 = [PPS, M1]

	return render(request, 'subjectview_sem2.html' ,{'sem2':sem2})


def subjectview_sem4(request): 
	M1 = subject()
	

	PPS = subject()

		
	sem4 = [PPS, M1]

	return render(request, 'subjectview_sem4.html' ,{'sem4':sem4})

def subjectview_sem5(request): 
	M1 = subject()
	


	PPS = subject()

		
	sem5 = [PPS, M1]

	return render(request, 'subjectview_sem5.html' ,{'sem5':sem5})


def subjectview_sem6(request): 
	M1 = subject()
	


	PPS = subject()

		
	sem6 = [PPS, M1]

	return render(request, 'subjectview_sem6.html' ,{'sem6':sem6})



def subjectview_sem7(request): 
	M1 = subject()
	


	PPS = subject()

		
	sem7 = [PPS, M1]

	return render(request, 'subjectview_sem7.html' ,{'sem7':sem7})


def subjectview_sem8(request): 
	M1 = subject()
	


	PPS = subject()

		
	sem8 = [PPS, M1]

	return render(request, 'subjectview_sem8.html' ,{'sem8':sem8})


def home(request):
	return render(request,'home.html')

def it_sems(request):
	return render(request,'it_sems.html') 

def cse_sems(request):
	return render(request,'cse_sems.html') 

def ece_sems(request):
	return render(request,'ece_sems.html') 

def eee_sems(request):
	return render(request,'eee_sems.html')

def it_sem1(request):
	return render(request,'it_sem1.html') 

def it_sem2(request):
	return render(request,'it_sem2.html')  

def it_sem3(request):
	return render(request,'it_sem3.html') 

def it_sem4(request):
	return render(request,'it_sem4.html') 

def it_sem5(request):
	return render(request,'it_sem5.html') 

def it_sem3_DMA(request):
	return render(request,'it_sem3_DMA.html') 

