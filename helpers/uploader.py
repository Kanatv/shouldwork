from youtube_upload.auth import GoogleAuth
from youtube_upload.youtube import Youtube

from config import Config

from translations import Messages as tr

import os
import time
import traceback

class Uploader:

    def __init__(self, file, title=None):
        
        self.file = file
        
        self.title = title


    async def start(self, progress=None, *args):
        self.progress = progress
        self.args = args

        await self._upload()

        return self.status, self.message


    async def _upload(self):
        try:

            auth = GoogleAuth(Config.CLIENT_ID, Config.CLIENT_SECRET)
            
            if not os.path.isfile(Config.CRED_FILE):
                self.status = False
                
                self.message = "Upload failed because you did not authenticate me."
                
                return

            auth.LoadCredentialsFile(Config.CRED_FILE)

            google = auth.authorize()

            properties = dict(
                title = self.title if self.title else os.path.basename(self.file),
                description = 'ezelpart54,ezelpart55,ezelpart56,ezelpart57,ezelpart58,ezelpart59ezelpart60,ezelpart61,ezelpart62,ezelpart63,ezeldramapart45,ezeldramapart48,ezeldrama,newpartezeldrama,newpartezel,ezeldramaamharic,kanatv,kanatelevisionezel,ezel,ezeldramapart45,ezelkanatvdrama,ezelkanatv,ezelturkishdrama,ezelturkishseries,ezelfilm,ezelpart44kanatv,ezelpart50,ezelpart44,KanaTV,firdegnochu,ferdegnochu,endeenat,buzutube,yalalekefikir,ezal,ezele,ኢዘልክፋል45,ኢዘልክፋል46,ኢዘልክፋል,47,ኢዘልክፋል48,ኢዘልክፋል49,ኢዘልክፋል50,,ezelpart55,ezelamharic,ezelamharicpart66ezelamharicpart67,ezelamharicpart58,ezelamharicpart63,ezelamharicpart61,ezelamharicpart62,ezelamharicpart64,ezelamharicpart65,ezelamharicpart57,ezelamharicpart63,ezelamharicpart60,ezelamharicpart59,ezelamharicpart65,ፍርደኞቹምእራፍ2ክፍል100ፍርደኞቹምእራፍ2ክፍል101,ፍርደኞቹምእራፍ2ክፍል10,ፍርደኞቹምእራፍ2ክፍል99,ፍርደኞቹምእራፍ2ክፍል103,ፍርደኞቹምእራፍ2ክፍል104,ፍርደኞቹምእራፍ2ክፍል105,feredenochupart97,feredenochupart98,feredenochupart99,feredenochupart100,feredenochupart101,ፍርደኞቹምእራፍ2ክፍል93,ፍርደኞቹምእራፍ2ክፍል92,ፍርደኞቹምእራፍ2ክፍል91,ፍርደኞቹምእራፍ2ክፍል94,feredenochupart85,feredenochupart86,feredenochupart87,feredenochupart88,feredenochupart89,feredenochupart90,feredenochupart91,ፍርደኞቹpart93,feredenochu,feredenochu90,,feredenochuseason2part97–kanatvamharicdrama,feredenochukanatv,feredenochupart89–kanatvamharicdrama,feredenochuseason2part95,feredenochuseason2part94,feredenochuseason2part93,feredenochuseason2part92,feredenochuseason2part91,feredenochuseason2,feredenochuseason2part90–kanatvamharicdrama,feredenochuseason2part96,feredenochupart2–kanatv,feredenochukanatvpart101,feredenochukanatvpart102,feredenochukanatvpart100,feredenochukanatvpart99,feredenochukanatvpart103,feredenochukanatvpart104,feredenochukanatvpart98,feredenochukanatvpart105,feredenochukanatvpart106,feredenochukanatvpart97,feredenochukanatvpart99,feredenochukanatvpart100,feredenochukanatvpart101,feredenochukanatvpart102,feredenochukanatvpart103,feredenochukanatvpart104,feredenochukanatvpart105,feredenochukanatvpart106,feredenochukanatvpart107,feredenochukanatvpart108,feredenochu,kanatvpart109,feredenochukanatvpart110,feredenochukanatvpart111,feredenochukanatvpart91,kanatv,feredenochuseason2,feredenochupart2',
                category = 27,
                privacyStatus = 'public'
            )

            youtube = Youtube(google)

            self.start_time = time.time()
            self.last_time = self.start_time

            r = await youtube.upload_video(video = self.file, properties = properties)

            self.status = True
            self.message = f"https://youtu.be/{r['id']}"
        except Exception as e:
            traceback.print_exc()
            self.status = False
            self.message = f"Error occuered during upload.\nError details: {e}"
        return

