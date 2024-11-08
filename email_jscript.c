#include <stdio.h>

typedef unsigned int bool;

bool is_character(char c)
{
	return ((c >= 'a') && (c <= 'z')) ||
		((c >= 'A') && (c <= 'Z')) ||
		((c >= '0') && (c <= '9'));
}

bool is_email(char *email_addr)
{
	/* Easy things first.  Start with a char */
	if (!is_character(email_addr[0]))
		return 0;
	
	int at_loc = -1;
	int dot_loc = -1;
	int i = 0;
	for (; email_addr[i] != '\0'; i++) {
		if (email_addr[i] == '@') 
			at_loc = i;
		if (email_addr[i] == '.')
			dot_loc = i;
	}
	int email_length = i - 1;

	/* Both a dot and @ must be present */
	if ((at_loc == -1) || (dot_loc == -1))
		return 0;

	/* Both dot and @ cannot be at the beginning or end */
	if ((at_loc == 0) || (dot_loc == 0))
		return 0;

	if ((at_loc == email_length) || (dot_loc == email_length))
		return 0;

	/* No other tests hold, so hopefully this is a valid email addr. */
	return 1;
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
		printf("ERROR: Wrong email address.");

	return 0;
}
