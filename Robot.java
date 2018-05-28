/*----------------------------------------------------------------------------*/
/* Copyright (c) 2017-2018 FIRST. All Rights Reserved.                        */
/* Open Source Software - may be modified and shared by FRC teams. The code   */
/* must be accompanied by the FIRST BSD license file in the root directory of */
/* the project.                                                               */
/*----------------------------------------------------------------------------*/

package org.usfirst.frc.team4026.robot;

import edu.wpi.first.networktables.NetworkTable;
import edu.wpi.first.networktables.NetworkTableEntry;
import edu.wpi.first.networktables.NetworkTableInstance;
import edu.wpi.first.wpilibj.IterativeRobot;
import edu.wpi.first.wpilibj.smartdashboard.SmartDashboard;

public class Robot extends IterativeRobot {

	boolean value;
	//Declare your Instances/Tables/Entries
	static NetworkTableInstance inst;
	NetworkTable operatorTable;
	NetworkTableEntry gotCubeEntry;

	@Override
	public void robotInit() {
		/*
		Initialize your Instances/Tables/Entries
		You can usually get away with using the Default Instance created with SmartDashboard
		Remember the keys you set here as that is how you access them later in the Python script
		*/
		inst = NetworkTableInstance.getDefault();
		operatorTable = inst.getTable("operator");
		gotCubeEntry = operatorTable.getEntry("gotCube");

	}

	@Override
	public void robotPeriodic() {
		SmartDashboard.putBoolean("connected", inst.isConnected());
		SmartDashboard.putBoolean("gotCube", gotCubeEntry.getBoolean(false));
	}

	@Override
	public void teleopPeriodic() {
		//Use forceSetBoolean to force the entry to be a boolean and overwrite whatever it was before
		gotCubeEntry.forceSetBoolean(true);
		// Retrieve the value from then entry using getBoolean or whatever applicable data type like getDouble
		value = gotCubeEntry.getBoolean(false);
	}


	@Override
	public void disabledPeriodic() {
		gotCubeEntry.forceSetBoolean(false);
	}
}
