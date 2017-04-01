from django.core.urlresolvers import reverse
from django.test import TestCase

# Create your tests here.
from minerals.models import Mineral


class MineralViewsTests(TestCase):
    def setUp(self):
        self.mineral = Mineral.objects.create(
          name="A Rock",
          image_filename="imagefile",
          image_caption="imagetitle",
          category="hard",
          formula="some fomular",
          strunz_classification="whats classified",
          crystal_system="oooooh",
          unit_cell="lots of them",
          color="dirty",
          crystal_symmetry="not",
          cleavage="notewothy",
          mohs_scale_hardness="rock hard",
          luster="smooth",
          streak="when broken",
          diaphaneity="???",
          optical_properties="looks like a rock",
          refractive_index="nope",
          crystal_habit="under pressure",
          specific_gravity="does not float",
          group="dirt")

    def test_mineral_list_redirect(self):
        """Test that mineral list with no pk will redirect"""
        resp = self.client.get(reverse('minerals:list'))
        self.assertEqual(resp.status_code, 302)

    def test_mineral_list_A(self):
        """Test mineral list, pk=A"""
        resp = self.client.get(reverse('minerals:list',
                                       kwargs={'pk': 'A'}))
        # Gets coeect response
        self.assertEqual(resp.status_code, 200)
        # Uses the correct template
        self.assertTemplateUsed(resp, 'minerals/mineral_list.html')
        # Uses the addins
        self.assertTemplateUsed(resp, 'category_list.html')
        self.assertTemplateUsed(resp, 'group_list.html')
        self.assertTemplateUsed(resp, 'letter_list.html')
        # Contains our setup object
        self.assertContains(resp, "A Rock")
        # Does not contain an item starting H
        self.assertNotContains(resp, "Hydrogrossular")
        # The A has the class current (hilite)
        self.assertContains(resp,
                            '<a class="current" href="/A/">A</a>',
                            html=True)
        # The B does not have the class current
        self.assertNotContains(resp,
                               '<a class="current" href="/B/">B</a>',
                               html=True)

    def test_mineral_list_group(self):
        resp = self.client.get(reverse('minerals:list',
                                       kwargs={'pk': 'group/dirt'}))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'minerals/mineral_list.html')
        self.assertContains(resp, "A Rock")
        self.assertNotContains(resp, "Hydrogrossular")
        self.assertContains(
            resp,
            '<a class="current" href="/group/dirt/">dirt (1)</a>',
            html=True)

    def test_mineral_list_category(self):
        resp = self.client.get(reverse('minerals:list',
                                       kwargs={'pk': 'category/hard'}))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'minerals/mineral_list.html')
        self.assertContains(resp, "A Rock")
        self.assertNotContains(resp, "Hydrogrossular")
        self.assertContains(
            resp,
            '<a class="current" href="/category/hard/">hard (1)</a>',
            html=True)

    def test_mineral_detail_view(self):
        resp = self.client.get(reverse('minerals:detail',
                                       kwargs={'pk': self.mineral.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.mineral, resp.context['mineral'])
        self.assertTemplateUsed(resp, 'minerals/mineral_detail.html')
        self.assertTemplateUsed(resp, 'category_list.html')
        self.assertTemplateUsed(resp, 'group_list.html')
        self.assertTemplateUsed(resp, 'letter_list.html')
        self.assertNotContains(resp, 'class="current"', html=True)

    def test_mineral_random_view(self):
        resp = self.client.get(reverse('minerals:random'))
        resp2 = self.client.get(reverse('minerals:random'))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.mineral, resp.context['mineral'])
        self.assertTemplateUsed(resp, 'minerals/mineral_detail.html')
        self.assertTemplateUsed(resp, 'category_list.html')
        self.assertTemplateUsed(resp, 'group_list.html')
        self.assertTemplateUsed(resp, 'letter_list.html')
        self.assertNotEqual(resp, resp2)
