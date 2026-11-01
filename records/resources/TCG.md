---
records:
    - id: TCG4NCP664
      kind: monograph
      title: The Classification of Quasithin Groups
      creators:
        - name: Michael Aschbacher
          role: author
        - name: Stephen Smith
          role: author
      date: "2004-11-02"
      msc:
        - code: 20D05
          from: zbmath_search
        - code: 20-02
          from: zbmath_search
        - code: 20D06
          from: zbmath_search
        - code: 20D08
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2004-11-02"
          ids:
            doi:
                - 10.1090/surv/111
                - 10.1090/surv/112
            zbl: "1065.20023"
            zbl_id: "2122847"
          manifestations:
            - key: m1
              kind: print
              publisher: American Mathematical Society
              date: "2004-11-02"
              ids:
                isbn:
                    - "9780821834107"
                    - "9781470413385"
              access:
                class: record
            - key: m2
              kind: print
              publisher: American Mathematical Society
              date: "2004-11-02"
              ids:
                isbn:
                    - "9780821834114"
                    - "9781470413392"
              access:
                class: record
      relations:
        - kind: part_of
          to: M891DMMNP3
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.14 scope/1
      catalogue:
        - source: ams-series
          snapshot: blake3:caf23f13a44130cfaf0ea65e08f1b670683c2f34af9ccb44343f3bca428b1013
          native_id: 10.1090/surv/111
          level: work
        - source: ams-series
          snapshot: blake3:caf23f13a44130cfaf0ea65e08f1b670683c2f34af9ccb44343f3bca428b1013
          native_id: 10.1090/surv/112
          level: work
        - source: zbmath_search
          snapshot: blake3:c337ce98d6a5f313c8656eac90c3348668181c9ed20fe8fe7554afd8dc3904ca
          native_id: "2122847"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
        - op: scope
          at: "2026-11-01"
          by: m2 v0.6.13 scope/1
          note: from in to in
---
