from unittest import TestCase
import os

from sabnzbd_copy import SabnzbdCopy

class TestSabnzbdCopy(TestCase):

  def get_path(self, relative_path):
    script_dir = os.path.dirname(os.path.realpath(__file__))
    script_dir = os.path.join(script_dir,"../../resources/")
    return os.path.join(script_dir,relative_path)
   

  def test_get_largest_file(self):
    copy = SabnzbdCopy()
    test_dir = self.get_path("exampleDownload")
    self.assertEqual(os.path.join(test_dir,"file.mkv"),copy.get_largest_file(test_dir))
  
  def test_get_largest_file2(self):
    copy = SabnzbdCopy()
    test_dir = self.get_path("exampleDownload2")
    self.assertEqual(os.path.join(test_dir,"subdir/file.mkv"),copy.get_largest_file(test_dir))
  
  def test_get_directory_to_move_to(self):
    copy = SabnzbdCopy()
    config_path = self.get_path("test_config.json")
    self.assertTrue(copy.read_configuration(config_path))
    self.assertEqual("Serien/This week tonight",copy.get_directory_to_move_to("this.week.tonight.s02e31.720p.mkv", "tvshows"))
    self.assertEqual("Serien/This week tonight",copy.get_directory_to_move_to("This.Week.Tonight.S01E08.720p.HDTV.mkv", "tvshows"))
    self.assertEqual("Serien/This week tonight",copy.get_directory_to_move_to("this week tonight s02e31720p.hdtv.x264.mkv", "tvshows"))
    self.assertEqual("Serien/Ted vs. Evil",copy.get_directory_to_move_to("/test/Ted.vs.Evil.S01E01.720p.mkv", "tvshows"))
    self.assertEqual("Serien/temp",copy.get_directory_to_move_to("test.mkv", "tvshows"))
    self.assertEqual("Serien/temp",copy.get_directory_to_move_to(" Ted.vs.Evil.S06E10.mkv", "tvshows"))
    self.assertEqual("Serien/The Theory",copy.get_directory_to_move_to("Theory.S01E01.mkv", "tvshows"))
    self.assertEqual("Serien/The Theory",copy.get_directory_to_move_to("The.Theory.S01E01.mkv", "tvshows"))
    self.assertEqual("Serien/You're the best",copy.get_directory_to_move_to("Youre.the.best.S01E01.mkv", "tvshows"))
    self.assertEqual("Serien/You're the best",copy.get_directory_to_move_to("You're.the.best.S01E01.mkv", "tvshows"))
    self.assertEqual("Filme",copy.get_directory_to_move_to("test.mkv", "movies"))
