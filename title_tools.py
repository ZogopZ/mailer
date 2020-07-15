from datetime import timedelta


class Title:

    def __init__(self, start_time, end_time, current_time):
        # Calculate the time that the user will be working from the
        # start until the end of his contract.
        full_time = (end_time +
                     timedelta(hours=8) -
                     start_time).total_seconds()
        # Calculate the time that the user has worked from the start of
        # his contract until now.
        lapsed_time = (current_time - start_time).total_seconds()
        # Calculate the percentage of time passed.
        self.evaluation = lapsed_time/full_time

    def military_title(self):
        title = ''
        # 'title' is a variable chosen between 19 values depending on
        # the value of 'self.evaluation' variable
        if 0 <= self.evaluation <= 0.0526:
            title = 'Στρατιώτης'
        elif 0.0526 < self.evaluation <= (2*0.0526):
            title = 'Υποδεκανέας'
        elif 2*0.0526 < self.evaluation <= (3*0.0526):
            title = 'Δεκανέας'
        elif 3*0.0526 < self.evaluation <= (4*0.0526):
            title = 'Λοχίας'
        elif 4*0.0526 < self.evaluation <= (5*0.0526):
            title = 'Επιλοχίας'
        elif 5*0.0526 < self.evaluation <= (6*0.0526):
            title = 'Αρχιλοχίας'
        elif 6*0.0526 < self.evaluation <= (7*0.0526):
            title = 'Ανθυπασπιστής'
        elif 7*0.0526 < self.evaluation <= (8*0.0526):
            title = 'Δόκιμος Έφεδρος Αξιωματικός'
        elif 8*0.0526 < self.evaluation <= (9*0.0526):
            title = 'Ανθυπολοχαγός'
        elif 9*0.0526 < self.evaluation <= (10*0.0526):
            title = 'Υπολοχαγός'
        elif 10*0.0526 < self.evaluation <= (11*0.0526):
            title = 'Λοχαγός'
        elif 11*0.0526 < self.evaluation <= (12*0.0526):
            title = 'Ταγματάρχης'
        elif 12*0.0526 < self.evaluation <= (13*0.0526):
            title = 'Αντισυνταγματάρχης'
        elif 13*0.0526 < self.evaluation <= (14*0.0526):
            title = 'Συνταγματάρχης'
        elif 14*0.0526 < self.evaluation <= (15*0.0526):
            title = 'Ταξίαρχος'
        elif 15*0.0526 < self.evaluation <= (16*0.0526):
            title = 'Υποστράτηγος'
        elif 16*0.0526 < self.evaluation <= (17*0.0526):
            title = 'Αντιστράτηγος'
        elif 17*0.0526 < self.evaluation <= (18*0.0526):
            title = 'Στρατηγός'
        elif 18*0.0526 < self.evaluation <= (19*0.0526):
            title = 'Στρατάρχης'
        return title
