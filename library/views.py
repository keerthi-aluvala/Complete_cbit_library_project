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



	POM = subject()
	POM.subject_name = 'POM'
	POM.pdf_link1 = 'POM_unit1.pdf'
	POM.pdf_link2 = 'POM_unit2.pdf'
	POM.pdf_link3 = 'POM_unit3.pdf'
	POM.pdf_link4 = 'POM_unit4.pdf'
	POM.pdf_link5 = 'POM_unit5.pdf'

	POM.content1 = 'Management: Definition of management, science or art, manager vs entrepreneur; managerial roles and skills;. Evolution of management, Basic management theories by FW Taylor, Henry Fayol, Types of Business Organizations, sole proprietorship, partnership, company, public and private enterprises; Organization culture and environment; Current trends and issues in management.'
	POM.content2 = 'Planning: Nature and purpose of Planning, types of Planning, objectives, setting objectives, policies, Strategic Management, Planning Tools and Techniques, Planning plant location and layout, Decision making steps & processes.'
	POM.content3 = 'Organizing: Nature and purpose of Organizing, formal and informal organization, organization structure, types, line and staff authority, departmentalization, delegation of authority, centralization and decentralization, job design, human resource management, HR planning, Recruitment selection, Training & Development, Performance Management, Career planning and Management.' 
	POM.content4 = 'Directing: Individual and group behavior, motivation, motivation theories, motivational techniques, job satisfaction, job enrichment, leadership, types & theories of leadership, effective communication.'
	POM.content5 = 'Controlling: system and process of controlling, budgetary and non-budgetary control techniques, use of computers and IT in management control, productivity problems and management, control and performance, direct and preventive control, reporting.'



	BEE = subject()
	BEE.subject_name = 'BEE'
	BEE.pdf_link1 = 'BEE_unit1.pdf'
	BEE.pdf_link2 = 'BEE_unit2.pdf'
	BEE.pdf_link3 = 'BEE_unit3.pdf'
	BEE.pdf_link4 = 'BEE_unit4.pdf'
	BEE.pdf_link5 = 'BEE_unit5.pdf'

	BEE.content1 = 'DC Circuits Electrical circuit elements (R, L and C), voltage and current sources, Kirchoff current and voltage laws, analysis of simple circuits with dc excitation, Superposition, Thevenin and Norton Theorems, Time-domain analysis of firstorder RL and RC circuits.'
	BEE.content2 = 'AC Circuits Representation of sinusoidal waveforms, peak and rms values, phasor representation, real power, reactive power, apparent power, power factor, Analysis of single-phase ac circuits consisting of R, L, C, RL, RC, RLC combinations (series and parallel). Three phase balanced circuits, voltage and current relations in star and delta connections.'
	BEE.content3 = 'Transformers Construction, Working principle, EMF Equation, Ideal and Practical transformer, Equivalent circuit of Transformer, OC and SC tests on a transformer, Efficiency and Regulation, Auto transformer.'
	BEE.content4 = 'DC and AC Machines DC Generators: Construction, Principle of operation, EMF equation, Classification, Characteristics of shunt, series and compound generators. DC Motors: Classification, Torque equation, Characteristics, Efficiency, Speed Control of Series and Shunt Motors. Three - Phase Induction Motors: Construction, Principle of operation, Torque equation, torque-slip characteristics, Power stages, speed control of induction motors.'
	BEE.content5 = 'Electrical Installations Electrical Wiring: Types of wires and cables, Electrical Safety precautions in handling electrical appliances, electric shock, first aid for electric shock, safety rules. Components of LT Switchgear: Switch Fuse Unit (SFU), MCB, ELCB, MCCB, Earthing, Elementary calculations for energy consumption.'
	
	sem3 = [DMA, DSA, BEE, BE, POM]

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

