from datetime import timedelta
import base64

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
        title_list = []
        title = ''
        img_path = ''
        enc_image = ''
        # 'title' is a variable chosen between 19 values depending on
        # the value of 'self.evaluation' variable
        if 0 <= self.evaluation <= 0.0526:
            title = 'Στρατιώτης'
            img_path = 'assets/army-insignia/stratiotis.png'
        elif 0.0526 < self.evaluation <= (2*0.0526):
            title = 'Υποδεκανέας'
            img_path = 'assets/army-insignia/upodekaneas.png'
        elif 2*0.0526 < self.evaluation <= (3*0.0526):
            title = 'Δεκανέας'
            img_path = 'assets/army-insignia/dekaneas.png'
        elif 3*0.0526 < self.evaluation <= (4*0.0526):
            title = 'Λοχίας'
            img_path = 'assets/army-insignia/loxias.png'
        elif 4*0.0526 < self.evaluation <= (5*0.0526):
            title = 'Επιλοχίας'
            img_path = 'assets/army-insignia/epiloxias.png'
        elif 5*0.0526 < self.evaluation <= (6*0.0526):
            title = 'Αρχιλοχίας'
            img_path = 'assets/army-insignia/arxiloxias.png'
        elif 6*0.0526 < self.evaluation <= (7*0.0526):
            title = 'Ανθυπασπιστής'
            img_path = 'assets/army-insignia/anthupaspistis'
        elif 7*0.0526 < self.evaluation <= (8*0.0526):
            title = 'Δόκιμος Έφεδρος Αξιωματικός'
            img_path = 'assets/army-insignia/dokimos_efedros.png'
        elif 8*0.0526 < self.evaluation <= (9*0.0526):
            title = 'Ανθυπολοχαγός'
            img_path = 'assets/army-insignia/anthupoloxagos.png'
        elif 9*0.0526 < self.evaluation <= (10*0.0526):
            title = 'Υπολοχαγός'
            img_path = 'assets/army-insignia/upoloxagos.png'
        elif 10*0.0526 < self.evaluation <= (11*0.0526):
            title = 'Λοχαγός'
            img_path = 'assets/army-insignia/loxagos.png'
        elif 11*0.0526 < self.evaluation <= (12*0.0526):
            title = 'Ταγματάρχης'
            img_path = 'assets/army-insignia/tagmatarxis.png'
        elif 12*0.0526 < self.evaluation <= (13*0.0526):
            title = 'Αντισυνταγματάρχης'
            img_path = 'assets/army-insignia/antisuntagmatarxis.png'
        elif 13*0.0526 < self.evaluation <= (14*0.0526):
            title = 'Συνταγματάρχης'
            img_path = 'assets/army-insignia/suntagmatarxis.png'
        elif 14*0.0526 < self.evaluation <= (15*0.0526):
            title = 'Ταξίαρχος'
            img_path = 'assets/army-insignia/taksiarxos.png'
        elif 15*0.0526 < self.evaluation <= (16*0.0526):
            title = 'Υποστράτηγος'
            img_path = 'assets/army-insignia/upostratigos.png'
        elif 16*0.0526 < self.evaluation <= (17*0.0526):
            title = 'Αντιστράτηγος'
            img_path = 'assets/army-insignia/antistratigos.png'
        elif 17*0.0526 < self.evaluation <= (18*0.0526):
            title = 'Στρατηγός'
            img_path = 'assets/army-insignia/stratigos.png'
        elif 18*0.0526 < self.evaluation <= (19*0.0526):
            title = 'Στρατάρχης'
            img_path = 'assets/army-insignia/stratarxis.png'
        with open(img_path, "rb") as img_file:
            enc_image = '<img src=\"data:image/png;base64,' +\
                        base64.b64encode(img_file.read()).decode('utf-8') +\
                        '" width="50" height="70" alt="base64 test">'
        title_list.extend([title, img_path, enc_image])
        return title_list
