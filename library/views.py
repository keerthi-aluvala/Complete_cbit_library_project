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
	
	ES = subject()
	ES.subject_name = 'ES'
	ES.pdf_link1 = 'ES_unit1.pdf'
	ES.pdf_link2 = 'ES_unit2.pdf'
	ES.pdf_link3 = 'ES_unit3.pdf'
	ES.pdf_link4 = 'ES_unit4.pdf'
	ES.pdf_link5 = 'ES_unit5.pdf'

	ES.content1 = 'Environmental Studies: Definition, Scope and importance, need for public awareness. Natural resources: Use and over utilization of Natural Resources - Water resources, Food resources, Forest resources, Mineral resources, Energy resources, Land resources.'
	ES.content2 = 'Ecosystems: Concept of an ecosystem, structure and function of an ecosystem, role of producers, consumers and decomposers, energy flow in an ecosystem, food chains, food webs, ecological pyramids, Nutrient cycling, Bio-geo chemical cycles, Terrestrial and Aquatic ecosystems.'
	ES.content3 = 'Biodiversity: Genetic, species and ecosystem biodiversity, Bio-geographical classification of India, India as a Mega diversity nation. Values of biodiversity, hot-spots of biodiversity, threats to biodiversity, endangered and endemic species of India, methods of conservation of biodiversity.'
	ES.content4 = 'Environmental Pollution: Cause, effects and control measures of air pollution, water pollution, marine pollution, soil pollution, noise pollution and Solid waste management, nuclear hazards Environmental Legislations: Environment protection Act, Air, Water, Forest & Wild life Acts, issues involved in enforcement of environmental legislation, responsibilities of state and central pollution control boards.'
	ES.content5 = 'Social issues and the environment: Water conservation methods: Rain water harvesting and watershed management, Environmental ethics, Sustainable development and Climate change: Global warming, Ozone layer depletion, forest fires, and Contemporary issues.'
	
	sem3 = [DMA, DSA, BEE, BE, POM, ES]

	return render(request, 'subjectview_sem3.html' ,{'sem3':sem3})

def subjectview_sem1(request): 
	ENG = subject()
	ENG.subject_name = 'ENG'
	ENG.pdf_link1 = 'ENG_unit1.pdf'
	ENG.pdf_link2 = 'ENG_unit2.pdf'
	ENG.pdf_link3 = 'ENG_unit3.pdf'
	ENG.pdf_link4 = 'ENG_unit4.pdf'
	ENG.pdf_link5 = 'ENG_unit5.pdf'

	ENG.content1 = 'Understanding Communication in English: Introduction, nature and importance of communication; Process of communication; Types of communication - verbal and non-verbal; Barriers to communication; Intrapersonal and interpersonal communication; Understanding Johari Window. Vocabulary &Grammar: The concept of Word Formation; Use of appropriate prepositions and articles.'
	ENG.content2 = 'Developing Writing Skills I: Paragraph writing. – Structure and features of a paragraph; Cohesion and coherence. Rearranging jumbled sentences. Email and Mobile etiquette. Vocabulary & Grammar: Use of cohesive devices and correct punctuation.'
	ENG.content3 = 'Developing Writing Skills II: Précis Writing; Techniques of writing precisely. Letter Writing – Structure, format of a formal letter; Letter of request and the response Vocabulary and Grammar: Subject-verb agreement. Use of prefixes and suffixes to form derivatives. Avoiding redundancies.'
	ENG.content4 = 'Developing Writing Skills III: Report writing – Importance, structure, elements of style of formal reports ; Writing a formal report. Vocabulary and Grammar: Avoiding ambiguity - Misplaced modifiers. Use of synonyms and antonyms.'
	ENG.content5 = 'Developing Reading Skills: The reading process, purpose, different kinds of texts; Reading comprehension; Techniques of comprehension – skimming, scanning, drawing inferences and conclusions. Vocabulary and Grammar: Words often confused; Use of standard abbreviations.'



	OSP = subject()
	OSP.subject_name = 'OSP'
	OSP.pdf_link1 = 'OSP_unit1.pdf'
	OSP.pdf_link2 = 'OSP_unit2.pdf'
	OSP.pdf_link3 = 'OSP_unit3.pdf'
	OSP.pdf_link4 = 'OSP_unit4.pdf'
	OSP.pdf_link5 = 'OSP_unit5.pdf'

	OSP.content1 = 'Wave Optics: Huygens’ principle –Superposition of waves –Interference of light by wave front splitting and amplitude splitting–Fresnel’s biprism – Interference in thin films in reflected light– Newton’s rings– Fraunhofer diffraction from a single slit –Double slit diffraction – Rayleigh criterion for limit of resolution– Concept of N-slits–Diffraction grating and its resolving power.'
	OSP.content2 = 'Lasers & Holography: Characteristics of lasers – Einstein’s coefficients –Amplification of light by population inversion –Different types of lasers: solid-state lasers: Ruby &Nd:YAG; gas lasers: He-Ne & CO2; semiconductor laser –Applications of lasers in engineering and medicine. Holography: Principle – Recording and reconstruction–Applications. Fiber Optics: Introduction –Construction –Principle –Propagation of light through an optical fiber – Numerical aperture and acceptance angle –Step-index and graded-index fibers –Pulse dispersion –Fiber losses–Fiber optic communication system –Applications.'
	OSP.content3 = 'Principles of Quantum Mechanics: Introduction –Wave nature of particles – de-Broglie hypothesis – Physical significance of ψ –Time-dependent and time-independent Schrodinger equations – Born interpretation – Probability current –Wave packets –Uncertainty principle –Particle in infinite square well potential –Scattering from potential step – Potential barrier and tunneling.'
	OSP.content4 = 'Band Theory of Solids: Salient features of free electron theory of metals (Classical and Quantum) – Fermi level –Density of states – Bloch’s theorem for particles in a periodic potential – Kronig-Penney model – Classification of solids: metals, semiconductors and insulators.'
	OSP.content5 = 'Semiconductors: Intrinsic and extrinsic semiconductors –Charge carrier concentration in intrinsic semiconductors –Dependence of Fermi level on carrier concentration and temperature in extrinsic semiconductors (qualitative) –Carrier generation and recombination –Carrier transport: diffusion and drift – P-N junction – Thermistor – Hall effect – LED –Solar cell.'



	PPS = subject()
	PPS.subject_name ='PPS'
	PPS.pdf_link1 = 'PPS_unit1.pdf'
	PPS.pdf_link2 = 'PPS_unit2.pdf'
	PPS.pdf_link3 = 'PPS_unit3.pdf'
	PPS.pdf_link4 = 'PPS_unit4.pdf'
	PPS.pdf_link5 = 'PPS_unit5.pdf'

	PPS.content1 = 'Introduction to computers and Problem Solving: Components of a computer, Operating system, compilers, Program Development Environments, steps to solve problems, Algorithm, Flowchart / Pseudocode with examples. Introduction to programming: Programming languages and generations, categorization of high-level languages. Introduction to C: Introduction, structure of C program, keywords, identifiers, Variables, constants, I/O statements, operators, precedence, and associativity.'
	PPS.content2 = 'Introduction to decision control statements: Selective, looping, and nested statements. Functions: Introduction, uses of functions, Function definition, declaration, passing parameters to functions, recursion, scope of variables and storage classes, Case study using functions and control statements.'
	PPS.content3 = 'Arrays: Introduction, declaration of arrays, accessing and storage of array elements, 1-dimensional array, Searching (linear and binary search algorithms) and sorting (Selection and Bubble) algorithms, 2-D arrays, matrix operations. Strings: Introduction, strings representation, string operations with examples. Case study using arrays.'
	PPS.content4 = 'Pointers: Understanding computer’s memory, introduction to pointers, declaration pointer variables, pointer arithmetic, pointers and strings, array of pointers, dynamic memory allocation, advantages, and drawbacks of pointers. Structures: Structure definition, initialization and accessing the members of a structure, nested structures, structures and functions, self- referential structures, unions, and enumerated data types.'
	PPS.content5 = 'Files: Introduction to files, file operations, reading data from files, writing data to files, error handing during file operations. Preprocessor Directives: Types of preprocessor directives, examples.'

	M1 = subject()
	M1.subject_name = 'M1'
	M1.pdf_link1 = 'M1_unit1.pdf'
	M1.pdf_link2 = 'M1_unit2.pdf'
	M1.pdf_link3 = 'M1_unit3.pdf'
	M1.pdf_link4 = 'M1_unit4.pdf'
	M1.pdf_link5 = 'M1_unit5.pdf'

	M1.content1 = 'Matrices: Rank of a matrix, Echelon form, consistency of linear System of equations, Linear dependence of vectors, Eigen values, Eigenvectors, Properties of Eigen values, Cayley-Hamilton theorem, Quadratic forms, Reduction of quadratic form to canonical form by linear transformation, Nature of quadratic form.'
	M1.content3 = 'Partial Differentiation and Its Applications :Functions of two or more variables, Partial derivatives, Higher order partial derivatives, Total derivative, Differentiation of implicit functions, Jacobians, Taylor’s expansion of functions of two variables, Maxima and minima of functions of two variables.'
	M1.content4 = 'Vector Differential Calculus: Scalar and vector point functions, vector operator Del, Gradient, Directional derivative, Divergence, Curl, Del applied twice to point functions, Del applied to product of point functions (vector identities). Applications: Irrotational fields and Solenoidal fields.'
	M1.content5 = 'Vector Integral Calculus: Line integral, Surface integral and Volume integral. Green’s theorem in the plane, verifications of Stroke’s theorem (without proof) and Gauss’s divergence theorem (without proof).'

	Calculus = subject()
	Calculus.subject_name = 'Calculus'
	Calculus.pdf_link1 = 'Calculus_unit1.pdf'
	Calculus.pdf_link2 = 'Calculus_unit2.pdf'
	Calculus.pdf_link3 = 'Calculus_unit3.pdf'
	Calculus.pdf_link4 = 'Calculus_unit4.pdf'
	Calculus.pdf_link5 = 'Calculus_unit5.pdf'

	Calculus.content1 = 'Matrices: Rank of a matrix, Echelon form, consistency of linear System of equations, Linear dependence of vectors, Eigen values, Eigenvectors, Properties of Eigen values, Cayley-Hamilton theorem, Quadratic forms, Reduction of quadratic form to canonical form by linear transformation, Nature of quadratic form.'
    Calculus.content3 = 'Partial Differentiation and Its Applications :Functions of two or more variables, Partial derivatives, Higher order partial derivatives, Total derivative, Differentiation of implicit functions, Jacobians, Taylor’s expansion of functions of two variables, Maxima and minima of functions of two variables.'
	Calculus.content4 = 'Vector Differential Calculus: Scalar and vector point functions, vector operator Del, Gradient, Directional derivative, Divergence, Curl, Del applied twice to point functions, Del applied to product of point functions (vector identities). Applications: Irrotational fields and Solenoidal fields.'
	Calculus.content5 = 'Vector Integral Calculus: Line integral, Surface integral and Volume integral. Green’s theorem in the plane, verifications of Stroke’s theorem (without proof) and Gauss’s divergence theorem (without proof).'
	
	sem1 = [ENG, OSP, PPS, M1, Calculus]

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

