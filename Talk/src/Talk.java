import java.io.*;
import java.net.*;

public class Talk 
{
	static int portNum = 12987;
	public static void Listen(String serverPortNumber)
	{
		InputStream in = null;
		String message = null;
		Socket client = null;
		ServerSocket server = null;
		int portNum;
		
		if(serverPortNumber != "" || serverPortNumber != " ")
		{
			portNum = Integer.parseInt(serverPortNumber);
		}
		else
		{
			portNum = 12987;
		}
		
		//checking port number
		try
		{
			server = new ServerSocket(portNum);
			System.out.println("Server listening on port " + portNum);
		}
		catch(IOException e)
		{
			System.out.println("Could not listen on port " + portNum);
			System.exit(-1);
		}
		
		//trying to accept the client
		try
		{
			client = server.accept();
			System.out.println("Server accepted connection from " + client.getInetAddress());
		}
		catch(IOException e)
		{
			System.out.println("Accept failed on port " + serverPortNumber);
			System.exit(-1);
		}
		
		//try to get inputStream from client
		try
		{
			in = client.getInputStream();
		}
		catch(IOException e)
		{
			System.out.println("Couldn't get an inputStream from the client");
			System.exit(-1);
		}
		
		//try to read what is being said by client
		try
		{
		
			byte[] tmp = new byte[1024];	
			while(true)
			{
				while(in.available() > 0)
				{
					int i = in.read(tmp, 0, 1024);
					if(i<0)break;
					System.out.println(new String(tmp, 0, i));
				}
				if(client.isClosed())
				{
					System.out.println("Exited");
					break;
				}
				try{Thread.sleep(1000);}catch(Exception ee){}
			}
		}
		catch(IOException e)
		{
			System.out.println("Read failed");
			System.exit(-1);
		}

		
		
	}//end listen
	
	public static void Talker(String serverName, String serverPortNumber)
	{
		if(serverPortNumber == "" || serverPortNumber == " ")
		{
			portNum = 12987;
		}
		else
		{
			portNum = Integer.parseInt(serverPortNumber);
		}
		
		Socket socket = new Socket();
		if(serverName == "" || serverName == " ")
		{
			serverName = socket.getLocalAddress().getHostAddress();
		}
		
		try
		{
			socket = new Socket(serverName, portNum);
			BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
			PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
			String message = "";
			while(in.ready())
			{
				message = in.readLine();
				out.println(message);
			}
		}
		catch(UnknownHostException e)
		{
			System.out.println("Unknown host: " + serverName);
			System.exit(-1);
		}
		catch(IOException e)
		{
			System.out.println("No I/O");
			System.exit(-1);
		}
	}//end talk

	public static void main(String[] args)
	{
		//gets the command
		String command = args[0];
		
		//chars and substring to help interpret the command
		char x = command.charAt(0);
		char y = command.charAt(1);
			
		//this is checking if the commands are valid
		if(x == '-')
		{	
			if(command.equals("help"))
			{
				System.out.println("My name is Eli Jones. \n"
						+ "To listen type -h[hostname | IP address][portnumber]\n"
						+ "To talk type -s[postnumber] \n"
						+ "To put in auto mode type -a[hostname | IP address][portnumber]");
			}//end help
			else
			{
				if(args[1] != null || args[2] != null)
				{
					String param1 = args[1];
					String param2 = args[2];
					
					if(y == 'h')
					{	
						System.out.println("listen command " + param1 + " " + param2);
						Listen(param2);
						
					}//end listen command
					else if(y == 's')
					{
						System.out.println("talk command " + param1 + " " + param2);
						Talker(param1, param2);
						
					}//end talk command
					else if(y == 'a')
					{
						System.out.println("auto command " + param1 + " " + param2);
						int portnumber = Integer.parseInt(param2);
						try
						{
							Socket socket = new Socket(param1, portnumber);
							if(!socket.isConnected())
							{
								Listen(param2);
							}
							else
							{
								Talker(param1, param2);
							}
						}
						catch(UnknownHostException e)
						{
							System.out.println("Unknown host: " + param1);
							System.exit(-1);
						}
						catch(IOException e)
						{
							System.out.println("No I/O");
							System.exit(-1);
						}
						
						
					}//end auto command
				}//end if
				else
				{
					System.out.println("This is not a command");
				}//end error
				
			}//end help else
		}//end "-" if
		else
		{
			System.out.println("Please enter a valid command or type -help for help");
		}//end error
	
	}//end main
}//end class
