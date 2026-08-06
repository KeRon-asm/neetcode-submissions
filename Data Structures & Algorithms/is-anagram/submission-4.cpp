class Solution {
public:
    bool isAnagram(string s, string t) {
        std::array<int, 26> s_list{}, t_list{};
        for(char letter: s){
            s_list[letter % 26] +=1;
        }
        for(char letter: t){
            t_list[letter % 26] +=1;
        }
        return s_list == t_list;
};
};