---
records:
    - id: GDRSSFFA5M
      kind: monograph
      title: Séminaire de Théorie du Potentiel Paris, No. 5
      creators:
        - name: Francis Hirsch
          role: editor
        - name: Gabriel Mokobodzki
          role: editor
      date: "1980"
      msc:
        - code: 00B15
          from: zbmath_search
        - code: 31-06
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: fr
          date: "1980"
          ids:
            doi: 10.1007/bfb0094144
            zbl: "0425.00009"
            zbl_id: "3661267"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1980"
              ids:
                isbn:
                    - "9783540100256"
                    - "9783540381891"
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
          native_id: 10.1007/bfb0094144
          level: work
        - source: zbmath_search
          snapshot: blake3:25dd7c4358839cf7c8c9f5d07f0562e94f38728153e7db2255a7191282b967c2
          native_id: "3661267"
          level: work
      history:
        - op: add
          at: "2026-11-01"
          by: m2 v0.6.13 cluster/1
        - op: split
          at: "2026-11-01"
          by: m2 v0.6.13 cluster/1
          note: split from V4D2YVABVV
        - op: scope
          at: "2026-11-01"
          by: m2 v0.6.13 scope/1
          note: to in
        - op: scope
          at: "2026-11-02"
          by: m2 dev scope/1
          note: from in to in
---
