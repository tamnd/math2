---
records:
    - id: BRWZVCTZX8
      kind: edited-volume
      title: Quantum Groups
      creators:
        - name: Pavel Etingof
          role: editor
        - name: Shlomo Gelaki
          role: editor
        - name: Steven Shnider
          role: editor
      date: "2007"
      msc:
        - code: 17-06
          from: zbmath_search
        - code: 00B25
          from: zbmath_search
        - code: 81R50
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2007"
          ids:
            doi: 10.1090/conm/433
            zbl: "1116.17001"
            zbl_id: "5169916"
          manifestations:
            - key: m1
              kind: print
              publisher: American Mathematical Society
              date: "2007"
              ids:
                isbn:
                    - "9780821837139"
                    - "9780821881125"
              access:
                class: record
      relations:
        - kind: part_of
          to: VAEN3CBGT1
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 dev scope/1
      catalogue:
        - source: ams-series
          snapshot: blake3:caf23f13a44130cfaf0ea65e08f1b670683c2f34af9ccb44343f3bca428b1013
          native_id: 10.1090/conm/433
          level: work
        - source: crossref_language
          snapshot: blake3:99510ada1a0f54f83dbf4ed97ef48852461d1f98d338d1a350cabf222fb85948
          native_id: 10.1090/conm/433
          level: work
        - source: zbmath_search
          snapshot: blake3:25dd7c4358839cf7c8c9f5d07f0562e94f38728153e7db2255a7191282b967c2
          native_id: "5169916"
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
          at: "2026-11-02"
          by: m2 dev scope/1
          note: from in to in
---
