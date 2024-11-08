#include <stdio.h>

typedef enum {false, true} bool;

bool is_character(char c)
{
	return ((c >= 'a') && (c <= 'z')) ||
		((c >= 'A') && (c <= 'Z')) ||
		((c >= '0') && (c <= '9'));
}

bool is_email(char *email_addr)
{
	int at_loc = -1;
	int dot_loc = -1;
	int i = 0;
	for (; email_addr[i] != '\0'; i++) {
		if ((email_addr[i] == '@') && (at_loc == -1))
			at_loc = i;
		if (email_addr[i] == '.')
			dot_loc = i;
		/* The case where non-alphanumeric characters besides the at sign, the underscore, and the period exist. */
		if ((email_addr[i] != '.') && (email_addr[i] != '@') && (email_addr[i] != '_') && (!is_character(email_addr[i])))
			return false;
	}
	int email_length = i - 1;

	/* A dot must present at least once; however
	 * @ must be present only once! */
	if ((at_loc == -1) || (dot_loc == -1))
		return false;

	/* Both dot and @ cannot be at the beginning or end */
	if ((at_loc == 0) || (dot_loc == 0))
		return false;

	if ((at_loc == email_length) || (dot_loc == email_length))
		return false;

	/* No other tests hold, so hopefully this is a valid email addr. */
	return true;
}

void print_jscript(char *email_addr)
{
	printf("javascript:location='mailto:");
	int i = 0;
	char c;
	while ((c = email_addr[i++]) != '\0') 
		printf("\\u00%x", c);
	printf("';void 0\n");
}

int main()
{
	char email[20] = "";
	printf("Enter email address: ");
	scanf("%s", email);

	if (is_email(email))
		print_jscript(email);
	else
		printf("ERROR: Wrong email address format.\n");

	return 0;
}
