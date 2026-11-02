---
records:
    - id: JC03HYT1KE
      kind: monograph
      title: Gorenstein Dimensions
      creators:
        - name: Lars Winther Christensen
          role: author
      date: "2000"
      msc:
        - code: 13D05
          from: zbmath_search
        - code: 13-02
          from: zbmath_search
        - code: 13D02
          from: zbmath_search
        - code: 18G10
          from: zbmath_search
        - code: 13D07
          from: zbmath_search
        - code: "13E05"
          from: zbmath_search
        - code: 13H10
          from: zbmath_search
        - code: 18G25
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2000"
          ids:
            doi: 10.1007/bfb0103980
            zbl: "0965.13010"
            zbl_id: "1544059"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "2000"
              ids:
                isbn:
                    - "9783540411321"
                    - "9783540400080"
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
          native_id: 10.1007/bfb0103980
          level: work
        - source: zbmath_search
          snapshot: blake3:25dd7c4358839cf7c8c9f5d07f0562e94f38728153e7db2255a7191282b967c2
          native_id: "1544059"
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
          by: m2 v0.6.17 scope/1
          note: from in to in
---
