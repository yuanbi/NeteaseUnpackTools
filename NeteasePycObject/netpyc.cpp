#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <map>
#include <string.h>

using namespace std;

#define TYPE_NULL '0'
#define TYPE_NONE 'N'
#define TYPE_FALSE 'F'
#define TYPE_TRUE 'T'
#define TYPE_STOPITER 'S'
#define TYPE_ELLIPSIS '.'
#define TYPE_INT 'i'
#define TYPE_INT64 'I'
#define TYPE_FLOAT 'f'
#define TYPE_COMPLEX 'x'
#define TYPE_LONG 'l'
#define TYPE_STRING 's'
#define TYPE_INTERNED 't'
#define TYPE_STRINGREF 'R'
#define TYPE_TUPLE '('
#define TYPE_LIST '['
#define TYPE_DICT '{'
#define TYPE_CODE 'c'
#define TYPE_UNICODE 'u'
#define TYPE_UNKNOWN '?'
#define TYPE_SET '<'
#define TYPE_FROZENSET '>'

map<int, int> decrypt_opcode = {{1, 38}, {2, 46}, {3, 37}, {4, 66}, {5, 12}, {10, 35}, {11, 67}, {12, 81}, {13, 32}, {15, 9}, {19, 63}, {20, 70}, {21, 44}, {22, 36}, {23, 39}, {24, 57}, {25, 10}, {26, 52}, {28, 49}, {30, 86}, {31, 87}, {32, 88}, {33, 89}, {40, 24}, {41, 25}, {42, 26}, {43, 27}, {50, 14}, {51, 15}, {52, 16}, {53, 17}, {54, 8}, {55, 21}, {56, 55}, {57, 82}, {58, 34}, {59, 22}, {60, 65}, {61, 6}, {62, 58}, {63, 71}, {64, 43}, {65, 30}, {66, 19}, {67, 5}, {68, 60}, {71, 53}, {72, 42}, {73, 3}, {74, 48}, {75, 84}, {76, 77}, {77, 78}, {78, 85}, {79, 47}, {80, 51}, {81, 54}, {82, 50}, {83, 83}, {84, 74}, {85, 64}, {86, 31}, {87, 72}, {88, 45}, {89, 33}, {90, 145}, {91, 159}, {92, 125}, {93, 149}, {94, 157}, {95, 132}, {96, 95}, {97, 113}, {98, 111}, {99, 138}, {100, 153}, {101, 101}, {102, 135}, {103, 90}, {104, 99}, {105, 151}, {106, 96}, {107, 114}, {108, 134}, {109, 116}, {110, 156}, {111, 105}, {112, 130}, {113, 137}, {114, 148}, {115, 172}, {116, 155}, {119, 103}, {120, 158}, {121, 128}, {122, 110}, {124, 97}, {125, 104}, {126, 118}, {130, 93}, {131, 131}, {132, 136}, {133, 115}, {134, 100}, {135, 120}, {136, 129}, {137, 102}, {140, 140}, {141, 141}, {142, 142}, {143, 94}, {146, 109}, {147, 123}, {106, 173}};

char* deal_pycodeobj(char *lp_data);

bool isEnecrypt = false; //为真表示 加密  为假表示解密

char decode_opcode(int opcode)
{
    unsigned char c_ret = 0x00;
    map<int, int>::iterator iter = decrypt_opcode.begin();

    while (iter != decrypt_opcode.end())
    {
        if (isEnecrypt == true)
        {
            if (iter->first == opcode)
            {

                c_ret = iter->second & 0x000000FF;
                return c_ret;
            }
        }
        else
        {
            if (iter->second == opcode)
            {
                c_ret = iter->first & 0x000000FF;
                return c_ret;
            }
        }
        iter++;
    }

    return 0xFF;
}

char *sub_type(char *lp_data, char type)
{
    switch (type)
    {
    case TYPE_NULL:
        break;
    case TYPE_NONE:
        break;
    case TYPE_FALSE:
        break;
    case TYPE_TRUE:
        break;
    case TYPE_STOPITER:
        break;
    case TYPE_ELLIPSIS:
        break;
    case TYPE_INT:
    {
        lp_data += 4; 
        break;
    }
    case TYPE_INT64:// no test
    {
        cout << "TYPE_INT64" << " -- >" << "no test!" << endl;
        lp_data += 8;
        break;
    }
    case TYPE_FLOAT:
    {
        cout << "TYPE_FLOAT" << " -- >" << "no test!" << endl;
        int n_count = 0;
        char c_count = *(lp_data++);
        n_count = (int)c_count;
        lp_data += n_count;
        break;
    }
    case TYPE_COMPLEX:// no test
    {
        cout << "TYPE_COMPLEX" << " -- >" << "no test!" << endl;
        int n_count = 0;
        char c_count = *(lp_data++);
        n_count = (int)c_count;
        lp_data += n_count;

        n_count = 0;
        c_count = *(lp_data++);
        n_count = (int)c_count;
        lp_data += n_count;
        break;
    }
    case TYPE_LONG:// no test
    {
        cout << "TYPE_LONG" << " -- >" << "no test!" << endl;
        
        int n_count = *(int *)lp_data;
        lp_data += 4;
        lp_data += n_count;
        break;
    }

    case TYPE_STRING:
    {
        int n_count = *(int *)lp_data;
        lp_data += 4;
        lp_data += n_count;
        break;
    }

    case TYPE_INTERNED:
    {
        int n_count = *(int *)lp_data;
        lp_data += 4;
        lp_data += n_count;
        break;
    }

    case TYPE_STRINGREF:
    {
        lp_data += 4;
        break;
    }

    case TYPE_TUPLE:
    {
        char c = 0x00;
        int n_count = *(int *)lp_data;
        lp_data += 4;
        for (int i = 0; i < n_count; i++)
        {
            c = *(lp_data++);
            lp_data = sub_type(lp_data, c);
        }
        break;
    }

    case TYPE_LIST: // no test
    {
        cout << "TYPE_LIST" << " -- >" << "no test!" << endl;

        char c = 0x00;
        int n_count = *(int *)lp_data;
        lp_data += 4;
        for (int i = 0; i < n_count; i++)
        {
            c = *(lp_data++);
            lp_data = sub_type(lp_data, c);
        }
        break;
    }

    case TYPE_DICT:// no test
    {
        cout << "TYPE_DICT must be error" << " -- >" << "no test!" << endl;

        char c = 0x00;
        while (1)
        {
            c = *(lp_data++); //key
            lp_data = sub_type(lp_data, c);

            if (c == 0x00)
                break; // need deal

            c = *(lp_data++); // value
            lp_data = sub_type(lp_data, c);
        }
        break;
    }

    case TYPE_CODE: //need deal
    {
        lp_data = deal_pycodeobj(lp_data);
        break;
    }

    case TYPE_UNICODE:
    {
        int n_count = *(int *)lp_data;
        lp_data += 4;
        lp_data += n_count;
        break;
    }

    case TYPE_UNKNOWN:// no test
    {
        cout << "TYPE_UNKNOWN" << " -- >" << "no test!" << endl;
        break;
    }

    case TYPE_SET:// no test
    {
        cout << "TYPE_SET" << " -- >" << "no test!" << endl;

        char c = 0x00;
        int n_count = *(int *)lp_data;
        lp_data += 4;

        for (int i = 0; i < n_count; i++)
        {
            c = *(lp_data++);
            lp_data = sub_type(lp_data, c);
        }

        break;
    }

    case TYPE_FROZENSET:// no test
    {
        cout << "TYPE_FROZENSET" << " -- >" << "no test!" << endl;

        char c = 0x00;
        int n_count = *(int *)lp_data;
        lp_data += 4;

        for (int i = 0; i < n_count; i++)
        {
            c = *(lp_data++);
            lp_data = sub_type(lp_data, c);
        }
        break;
    }

    default:
        cout << "error type" << endl;
        break;
    }
    return lp_data;
}

char *deal_opcode(char *lp_data)
{
    int n_count = *(int *)lp_data;
    lp_data += 4;

    int n_code = 0x00;
    for (int i = 0; i < n_count;)
    {
        // c_code = lp_data[i];
        n_code = lp_data[i] & 0x000000FF;
        unsigned char c = (char)(decode_opcode(n_code) & 0x000000FF);
        if (c == 0xFF)
        {
            cout << "Error opcode :" << n_code << endl;
            i++;
            continue;
        }
        

        lp_data[i] = c;

        if (c < 0x5A)
            i += 1;
        else
            i += 3;
    }

    lp_data += n_count;
    return lp_data;
}

char* deal_pycodeobj(char *lp_data)
{
    lp_data += 4;
    lp_data += 4;
    lp_data += 4;
    lp_data += 4;

    lp_data += 1; // 0x73
    lp_data = deal_opcode(lp_data);

    char c_type = 0x00;
    for (int i = 0; i < 9; i++)
    {
        if (i == 7)
        {
            lp_data += 4;
            continue;
        }
        c_type = *(lp_data++);
        lp_data = sub_type(lp_data, c_type);
    }
    return lp_data;
}

int main(int argc, char **argv)
{
    unsigned char magic_number[8] = {0x03,0xF3,0x0D,0x0A,0x00,0x00,0x00,0x00};
    if( argc < 3)
    {
        cout << "arg error\nnetpyc input_file_name(Maybe absolute path) output_file_name(Maybe absolute path) [is_Encrytry(0,1)(default 0)]\n" << endl;
        return 0;
    }

    if(argc >= 4)
    {
        if(argv[3][0] == '1')
            isEnecrypt = true;
    }

    // FILE *fp = fopen("/home/yuan/Desktop/stzb_patch/NeteasePycDecode/dumpx1.pyc", "rb");
    FILE *fp = fopen(argv[1], "rb");
    if (fp == NULL)
    {
        cout << "Input file read error" << endl;
        return 0;
    }

    fseek(fp, 0, SEEK_END);
    size_t len = ftell(fp);
    char *lp_buf = new char[len];
    // bzero(szBuf,0,len);
    fseek(fp, 0, SEEK_SET);
    int iRead = fread(lp_buf, 1, len, fp);
    fclose(fp);

    // lp_buf += 1; // 0x73

    deal_pycodeobj(lp_buf + 1);
    // isEnecrypt = true;

    // fp = fopen("/home/yuan/Desktop/stzb_patch/NeteasePycDecode/dumpx1_main.pyc", "wb");
    fp = fopen(argv[2], "wb");
    if (fp == NULL)
    {
        cout << "Input file read error" << endl;
        return 0;
    }

    fwrite(magic_number,1,8,fp);
    fwrite(lp_buf, 1, len, fp);
    fclose(fp);
    delete lp_buf;
    //     if (argc < 3)
    //     {  
    //         printf("error!\n");
    //         printf("./main str\n");
    //  
    //         return -1;
    //     }
}
