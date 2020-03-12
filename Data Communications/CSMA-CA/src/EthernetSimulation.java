import java.util.Random;

public class EthernetSimulation 
{
	
	private static int BackOff = 200;
	private static int IFS = 50; 
	private static int Wait = 200;
	private static int limit = 16;

	public static void main(String[] args) 
	{
		Random random = new Random();
		
		//print the title
		System.out.printf("%s %10s %11s %12s %6s\n %28s %11s %8s\n", 
				"Index", "Re-Trys", "RTS|CTS", "ACK|Data", "Max", "Failures", "Failures", "Slots");
		
		for(int i = 0; i < 25; i++)
		{
			//station has frame to send
			boolean tryagain = true; //while this is true the loop will loop through again
			int K = 0;
			int slots = 0;
			int ACKfail = 0;
			int RTSfail = 0;
			while(tryagain)
			{ 
				//channel is free
				long s = System.currentTimeMillis();
				while(System.currentTimeMillis() - s < IFS)
				{
					//do nothing
				}
				slots = (int)Math.pow(2, K) - 1;
					
				//send rts
					
				s = System.currentTimeMillis();
				while(System.currentTimeMillis() - s < Wait)
				{
					//do nothing
				}
					
				if(random.nextBoolean()) //CTS received before timeout?
				{
					s = System.currentTimeMillis();
					while(System.currentTimeMillis() - s < IFS)
					{
						//do nothing
					}
						
					//send frame
						
					s = System.currentTimeMillis();
					while(System.currentTimeMillis() - s < Wait)
					{
						//do nothing
					}
						
					if(random.nextBoolean()) //ACK received before timeout
					{
						//transmission was a success
						break;//this breaks the try again while loop
					}
					else
					{
						ACKfail++;
					}
						
				}//end if
				else 
				{
					RTSfail++;
				}
					
				K++;
					
				if(K > limit)
				{
					break;//this breaks the try again while loop
				}//end if
				
				s = System.currentTimeMillis();
				while(System.currentTimeMillis() - s < BackOff)
				{
					//do nothing
				}
					
			}//end try again
				
			
				System.out.printf("%4d %8d %11d %12d %10d\n", i+1, K, RTSfail, ACKfail, slots);
			
		}//end number of frames
		
		
	}//end main

}//end class
