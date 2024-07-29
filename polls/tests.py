from django.test import TestCase
import datetime
from dajngo.utils import timezone

from .models import Pergunta

class PerguntaModelTest(TestCase):
    def test_plucidada_recentemente_pergunta_no_futuro(self):
        """
        o método para pergunta no futuro deve terornar false
        """
        tempo = timezone.now() + datetime.timedelta(seconds = 1)
        p = Pergunta(data_pub = tempo)
        self.assertIs(p.publicada_recentemente(), False)