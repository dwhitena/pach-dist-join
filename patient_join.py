import pandas as pd
import uuid
import os

# Define directories.
inInfoDir = "/pfs/patient_info/"
inMeasurementsDir = "/pfs/patient_measurements/"
outDir = "/pfs/out/"

# Tag this worker to illustrate the process.
worker_name = str(uuid.uuid1())

# Loop over any info files.
i = 1
for info_file in os.listdir(inInfoDir):
    
    # Loop over any measurement files.
    for measurement_file in os.listdir(inMeasurementsDir):

        if measurement_file == info_file:
            
            # Read in the info data.
            df1 = pd.read_csv(inInfoDir + info_file).set_index('patient')

            # Read in the measurement data.
            df2 = pd.read_csv(inMeasurementsDir + measurement_file).set_index('patient')
            
            # Join the two dataframes.
            df = df1.join(df2)
            
            # Save the result.
            df.to_csv(outDir + worker_name + '_' + str(i) + '.csv')
            
            i += 1
