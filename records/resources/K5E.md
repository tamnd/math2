---
records:
    - id: K5EKQHDM4F
      kind: monograph
      title: SK1 von Schiefkörpern
      creators:
        - name: P. Draxl
          role: editor
        - name: M. Kneser
          role: editor
      date: "1980"
      msc:
        - code: "16E20"
          from: zbmath_search
        - code: 00Bxx
          from: zbmath_search
        - code: 16-06
          from: zbmath_search
        - code: 18F25
          from: zbmath_search
        - code: 16U60
          from: zbmath_search
        - code: 16Kxx
          from: zbmath_search
        - code: 16W99
          from: zbmath_search
        - code: 20G35
          from: zbmath_search
        - code: 16B50
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: de
          date: "1980"
          ids:
            doi: 10.1007/bfb0095915
            zbl: "0426.16022"
            zbl_id: "3663357"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1980"
              ids:
                isbn:
                    - "9783540097471"
                    - "9783540385998"
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
          native_id: 10.1007/bfb0095915
          level: work
        - source: zbmath_search
          snapshot: blake3:25dd7c4358839cf7c8c9f5d07f0562e94f38728153e7db2255a7191282b967c2
          native_id: "3663357"
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
