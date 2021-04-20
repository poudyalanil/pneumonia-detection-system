def email(image,title,content,link):

    html_format=f''' <!DOCTYPE html
    PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml"
    xmlns:o="urn:schemas-microsoft-com:office:office">

    <head>
    <title>{title}</title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0 " />
    <meta name="format-detection" content="telephone=no" />
    <!--[if !mso]><!-->
    <link href="https://fonts.googleapis.com/css?family=Lato:100,100i,300,300i,400,700,700i,900,900i"
        rel="stylesheet" />
    <!--<![endif]-->
    '''

    css = '''
    <style type="text/css">
        body {
            margin: 0;
            padding: 0;
            -webkit-text-size-adjust: 100% !important;
            -ms-text-size-adjust: 100% !important;
            -webkit-font-smoothing: antialiased !important;
        }

        img {
            border: 0 !important;
            outline: none !important;
        }

        p {
            Margin: 0px !important;
            Padding: 0px !important;
        }

        table {
            border-collapse: collapse;
            mso-table-lspace: 0px;
            mso-table-rspace: 0px;
        }

        td,
        a,
        span {
            border-collapse: collapse;
            mso-line-height-rule: exactly;
        }
    </style>
    </head>
    '''
    body = f'''




    <body class="em_body" style="margin:0px auto; padding:0px;" bgcolor="#efefef">
    <table width="100%" border="0" cellspacing="0" cellpadding="0" class="em_full_wrap" align="center"
        bgcolor="#efefef">
        <tr>
            <td align="center" valign="top">
                <table align="center" width="650" border="0" cellspacing="0" cellpadding="0" class="em_main_table"
                    style="width:650px; table-layout:fixed;">
                    <tr>
                        <td align="center" valign="top" style="padding:0 25px;" class="em_aside10">
                            <table width="100%" border="0" cellspacing="0" cellpadding="0" align="center">
                                <tr>
                                    <td height="26" style="height:26px;" class="em_h20">&nbsp;</td>
                                </tr>

                                <tr>
                                    <td height="28" style="height:28px;" class="em_h20">&nbsp;</td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
    <table width="100%" border="0" cellspacing="0" cellpadding="0" class="em_full_wrap" align="center"
        bgcolor="#efefef">
        <tr>
            <td align="center" valign="top">
                <table align="center" width="650" border="0" cellspacing="0" cellpadding="0" class="em_main_table"
                    style="width:650px; table-layout:fixed; background-color:#f8f8f8;">
                    <tr>
                        <td align="center" valign="top" style="padding:0 25px; background-color:#efefef;"
                            bgcolor="#efefef" class="em_aside10">
                            <table width="100%" border="0" cellspacing="0" cellpadding="0" align="center">

                                <tr>
                                    <td class="em_blue em_font_22" align="center" valign="top"
                                        style="font-family: Arial, sans-serif; font-size: 26px; line-height: 29px; color:#264780; font-weight:bold;">
                                        New Blog Alert!</td>
                                </tr>
                                <tr>
                                    <td height="22" class="em_h20" style="height:22px; font-size:0px; line-height:0px;">
                                        &nbsp;</td>
                                </tr>
                                <tr>
                                    <td valign="top" align="center"><a href="#" target="_blank"
                                            style="text-decoration:none;"><img
                                                src="{image}" width="600" height="230"
                                                class="em_full_img" alt="Alt tag goes here" border="0"
                                                style="display:block; max-width:600px; font-family:Arial, sans-serif; font-size:17px; line-height:20px; color:#000000; font-weight:bold;" /></a>
                                    </td>
                                </tr>
                                <tr>
                                    <td valign="top" align="left" bgcolor="#ffffff"
                                        style="padding-left:25px; padding-right:35px; background-color:#ffffff;"
                                        class="em_aside10">
                                        <table width="100%" border="0" cellspacing="0" cellpadding="0" align="left">
                                            <tr>
                                                <td height="22" style="height:22px;" class="em_h20">&nbsp;</td>
                                            </tr>
                                            <tr>
                                                <td class="em_blue em_center" align="left" valign="top"
                                                    style="font-family: Arial, sans-serif; font-size: 20px; line-height: 24px; color:#264780; font-weight:bold;">
                                                    Blog TITLE</td>
                                            </tr>
                                            <tr>
                                                <td height="8" style="height:8px; font-size:0px; line-height:0px;">
                                                    &nbsp;</td>
                                            </tr>
                                            <tr>
                                                <td class="em_grey em_center" align="left" valign="top"
                                                    style="font-family: Arial, sans-serif; font-size: 16px; line-height: 24px; color:#434343;">

    {content}                                                </td>
                                            </tr>
                                            <tr>
                                                <td height="16" style="height:16px; font-size:1px; line-height:1px;">
                                                    &nbsp;</td>
                                            </tr>

                                            <tr>
                                                <td align="left" valign="top">
                                                    <table width="140" border="0" cellspacing="0" cellpadding="0"
                                                        align="left" style="width:140px;" class="em_wrapper">
                                                        <tr>
                                                            <td valign="top" align="center">
                                                                <table width="140"
                                                                    style="width:140px; background-color:#6bafb2; border-radius:4px;"
                                                                    border="0" cellspacing="0" cellpadding="0"
                                                                    align="center" bgcolor="#6bafb2">
                                                                    <tr>
                                                                        <td class="em_white" height="34" align="center"
                                                                            valign="middle"
                                                                            style="font-family: Arial, sans-serif; font-size: 13px; color:#ffffff; font-weight:bold; height:34px;">
                                                                            <a href="{link}"
                                                                                target="_blank"
                                                                                style="text-decoration:none; color:#ffffff; line-height:34px; display:block;">Read More...</a></td>
                                                                    </tr>
                                                                </table>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                </td>
                                            </tr>
                                            <tr>
                                                <td height="26" style="height:26px;" class="em_h20">&nbsp;</td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>

                            </table>
                        </td>
                    </tr>
                    
                    
                </table>
            </td>
        </tr>
    </table>
    <table width="100%" border="0" cellspacing="0" cellpadding="0" class="em_full_wrap" align="center"
        bgcolor="#efefef">
        <tr>
            <td align="center" valign="top">
                <table align="center" width="650" border="0" cellspacing="0" cellpadding="0" class="em_main_table"
                    style="width:650px; table-layout:fixed;">
                    <tr>
                        <td align="center" valign="top" style="padding:0 25px;" class="em_aside10">
                            <table width="100%" border="0" cellspacing="0" cellpadding="0" align="center">
                                <tr>
                                    <td height="40" style="height:40px;" class="em_h20">&nbsp;</td>
                                </tr>

                                <tr>
                                    <td height="16" style="height:16px; font-size:1px; line-height:1px; height:16px;">
                                        &nbsp;</td>
                                </tr>
                                
                                <tr>
                                    <td height="10" style="height:10px; font-size:1px; line-height:1px;">&nbsp;</td>
                                </tr>
                                
                                
                                <tr>
                                    <td height="35" style="height:35px;" class="em_h20">&nbsp;</td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                    
                    <tr>
                        <td align="center" valign="top" style="padding:0 25px;" class="em_aside10">
                            <table width="100%" border="0" cellspacing="0" cellpadding="0" align="center">
                                
                                <tr>
                                    <td align="center" valign="top">
                                        <table border="0" cellspacing="0" cellpadding="0" align="left"
                                            class="em_wrapper">
                                            <tr>
                                                <td class="em_grey" align="center" valign="middle"
                                                    style="font-family: Arial, sans-serif; font-size: 11px; line-height: 16px; color:#434343;">
                                                    &copy; PDS 2021 &nbsp;|&nbsp; <a href="http://fyp.anilpoudyal.com.np/ target="_blank"
                                                        style="text-decoration:underline; color:#434343;">fyp.anilpoudyal.com.np</a>
                                                </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                                <tr>
                                    <td height="16" style="font-size:0px; line-height:0px; height:16px;">&nbsp;</td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                    
                </table>
            </td>
        </tr>
    </table>
    </body>

    </html>
    '''
 

    outgoing_email = html_format+css+body

    return outgoing_email