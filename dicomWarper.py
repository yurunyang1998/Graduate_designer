from dicompylercore.dicomparser import DicomParser


class dicomWarper(DicomParser):
    def __init__(self,rtstructfile):
        try:
            super(dicomWarper, self).__init__(rtstructfile)
        except Exception as e:
            print(e)

    def getstruct(self):
        return self.GetStructures()


    def removeOtherGTV(self,unremovedGTVname,savepath):


        lens = len(self.ds.StructureSetROISequence)
        for i in range(lens-1, -1, -1):
            if(self.ds.StructureSetROISequence[i].ROIName == unremovedGTVname):
                continue
            else:
                del self.ds.StructureSetROISequence[i]
                del self.ds.RTROIObservationsSequence[i]
                del self.ds.ROIContourSequence[i]

        self.ds.save_as(savepath+'/newrtfile.dcm', False)

if __name__ == '__main__':

    dw = dicomWarper("H:\\3DslicerData\\HMR\\002\\CTSTR\\rt000000.dcm")
    print(dw.getstruct())
    dw.removeOtherGTV("modPTV56")