from pages.base_page import BasePage


class Add_match(BasePage):
    my_team_field_xpath= "/html/body/div/div[1]/main/div[2]/form/div[2]/div/div[1]/div/div/input"
    enemy_team_field_xpath = "/html/body/div/div[1]/main/div[2]/form/div[2]/div/div[2]/div/label"
    my_team_score_field_xpath = "/html/body/div/div[1]/main/div[2]/form/div[2]/div/div[3]/div/label"
    enemy_team_score_xpath = "/html/body/div/div[1]/main/div[2]/form/div[2]/div/div[4]/div/label"
    date_field_xpath = "/html/body/div/div[1]/main/div[2]/form/div[2]/div/div[5]/div/label"
    calendar_button_xpath = "/html/body/div/div[1]/main/div[2]/form/div[2]/div/div[5]/div/div/input"
    match_at_home_check_box_xpath = "/html/body/div/div[1]/main/div[2]/form/div[2]/div/div[6]/fieldset/div/label[1]/span[2]"
    match_out_home_check_box_xpath = "/html/body/div/div[1]/main/div[2]/form/div[2]/div/div[6]/fieldset/div/label[2]/span[2]"
    number_field_xpath = "/html/body/div/div[1]/main/div[2]/form/div[2]/div/div[10]/div/label"
    t_shirt_color_field_xpath = "/html/body/div/div[1]/main/div[2]/form/div[2]/div/div[7]/div/label"
pass