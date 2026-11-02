---
records:
    - id: YF0NT5HWXB
      kind: monograph
      title: Potential Theory—Selected Topics
      creators:
        - name: Hiroaki Aikawwa
          role: author
        - name: Matts Essén
          role: author
      date: "1996"
      msc:
        - code: 31-02
          from: zbmath_search
        - code: 31B15
          from: zbmath_search
        - code: 31B05
          from: zbmath_search
        - code: 31A05
          from: zbmath_search
        - code: 31B25
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1996"
          ids:
            doi: 10.1007/bfb0093410
            zbl: "0865.31001"
            zbl_id: "945655"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1996"
              ids:
                isbn:
                    - "9783540615835"
                    - "9783540699910"
              access:
                class: record
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 dev scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0093410
          level: work
        - source: zbmath_search
          snapshot: blake3:25dd7c4358839cf7c8c9f5d07f0562e94f38728153e7db2255a7191282b967c2
          native_id: "945655"
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
