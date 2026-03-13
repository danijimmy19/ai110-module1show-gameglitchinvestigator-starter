from logic_utils import *

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == ("Win", "🎉 Correct!")

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == ("Too High", "📉 Go LOWER!")

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == ("Too Low", "📈 Go HIGHER!")


# ---------------------------
# get_range_for_difficulty
# ---------------------------

def test_easy_range():
    assert get_range_for_difficulty("Easy") == (1, 20)


def test_normal_range():
    assert get_range_for_difficulty("Normal") == (1, 50)


def test_hard_range():
    assert get_range_for_difficulty("Hard") == (1, 100)


def test_unknown_difficulty_defaults_to_normalish_range():
    low, high = get_range_for_difficulty("Impossible")
    assert isinstance(low, int)
    assert isinstance(high, int)
    assert low < high


# ---------------------------
# update_score
# ---------------------------

def test_update_score_win_awards_points():
    new_score = update_score(current_score=0, outcome="Win", attempt_number=3)
    assert new_score > 0


def test_update_score_win_has_minimum_floor():
    new_score = update_score(current_score=0, outcome="Win", attempt_number=50)
    assert new_score == 10


def test_update_score_wrong_guess_does_not_increase_score():
    new_score = update_score(current_score=20, outcome="Too Low", attempt_number=2)
    assert new_score <= 20


def test_update_score_unknown_outcome_leaves_score_unchanged():
    new_score = update_score(current_score=25, outcome="Something Else", attempt_number=1)
    assert new_score == 25