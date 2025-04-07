def prijati(request):
    uchazeci = [
        {"jmeno": "Jan Novák", "matematika": 85, "cestina": 78, "anglictina": 90},
        {"jmeno": "Petra Svobodová", "matematika": 92, "cestina": 88, "anglictina": 85},
        {"jmeno": "Karel Dvořák1", "matematika": 50, "cestina": 95, "anglictina": 86},
        {"jmeno": "Karel Dvořák2", "matematika": 54, "cestina": 96, "anglictina": 84},
        {"jmeno": "Karel Dvořák3", "matematika": 77, "cestina": 86, "anglictina": 87},
        {"jmeno": "Karel Dvořák4", "matematika": 48, "cestina": 94, "anglictina": 89},
        {"jmeno": "Karel Dvořák5", "matematika": 87, "cestina": 91, "anglictina": 88},
        {"jmeno": "Karel Dvořák6", "matematika": 80, "cestina": 85, "anglictina": 81},
        {"jmeno": "Karel Dvořák7", "matematika": 65, "cestina": 93, "anglictina": 82},
        {"jmeno": "Karel Dvořák8", "matematika": 75, "cestina": 92, "anglictina": 83},
        {"jmeno": "Karel Dvořák9", "matematika": 68, "cestina": 91, "anglictina": 84},
        {"jmeno": "Karel Dvořák10", "matematika": 90, "cestina": 75, "anglictina": 75},
        {"jmeno": "Karel Dvořák11", "matematika": 86, "cestina": 85, "anglictina": 69},
        {"jmeno": "Karel Dvořák12", "matematika": 85, "cestina": 65, "anglictina": 75},
        {"jmeno": "Karel Dvořák13", "matematika": 75, "cestina": 84, "anglictina": 79},
        {"jmeno": "Karel Dvořák14", "matematika": 74, "cestina": 99, "anglictina": 71},
        {"jmeno": "Karel Dvořák15", "matematika": 49, "cestina": 73, "anglictina": 80},
    
    ]
    print ('uchazeci')

    for matematika,cestina,anglictina in uchazeci:
        celkem = matematika + cestina + anglictina
        print(celkem)
        

    prijati = uchazeci.filter(matematika__lte=60,cestina__lte=60,anglictina__lte=60).order_by('celkem')

    print ('prijati')
